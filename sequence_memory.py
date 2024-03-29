from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from userdata import username, password

# The program works by searching some specific elements in DOM.
# Sometimes the element that the program looking for might not be present
# In those cases program waits for search_time amount of seconds before
# attempting to run the next instruction
search_time = 10

# Maximum rounds that the bot plays
max_rounds = 50

class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.login()
        self.playSequenceMemory()
        self.saveScore()

    def muteGame(self):
        WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.CLASS_NAME, 'fa-volume-up'))).click()

    def login(self):
        self.driver.get('https://humanbenchmark.com/login')
        username_input = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.NAME, 'username')))
        password_input = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.NAME, 'password')))

        username_input.send_keys(username)
        password_input.send_keys(password)

        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div/form/p[3]/input').click()
        sleep(1)

    def playSequenceMemory(self):
        self.driver.get('https://humanbenchmark.com/tests/sequence')
        self.muteGame()
        WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.XPATH, "//button[@class='css-de05nr e19owgy710']"))).click()

        squares = WebDriverWait(self.driver, search_time).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'square')))
        squares_item = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.CLASS_NAME, 'squares')))
        square_rows = []
        square_rows.append([])
        square_rows.append([])
        square_rows.append([])
        i = 0
        for s in squares:
            square_rows[i//3].append(s)
            i += 1

        round = 1
        while True:
            r = 0
            sequence = []
            activated_square = None
            prev_square = None

            while r < round:
                activated_square = WebDriverWait(squares_item, 99999).until(EC.presence_of_element_located((By.CLASS_NAME, 'active')))
                if prev_square == activated_square:
                    continue
                prev_square = activated_square
                for y in range(3):
                    for x in range(3):
                        if activated_square == square_rows[y][x]:
                            sequence.append((x, y))
                r += 1

            # Wait for all squares to be deactivated
            while True:
                break_loop = False
                try:
                    squares_item.find_element(By.CLASS_NAME, 'active')
                except:
                    break_loop = True
                if break_loop:
                    break

            # Lose on purpose
            if round > max_rounds:
                item = sequence[1]
                x = item[0]
                y = item[1]
                square_rows[y][x].click()
                break

            for item in sequence:
                x = item[0]
                y = item[1]
                square_rows[y][x].click()
            round += 1

    def saveScore(self):
        WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Save score')]"))).click()
        print("Press enter to close the program...", end='')
        input()
        self.driver.close()

def main():
    app = Application()

if __name__ == '__main__':
    main()

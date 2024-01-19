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
max_rounds = 100

def waitUntilDeactivated(item):
    while True:
        try:
            item.find_element(By.CLASS_NAME, 'active')
        except:
            return

class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.login()
        self.playVisualMemory()
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

    def playVisualMemory(self):
        self.driver.get('https://humanbenchmark.com/tests/memory')
        self.muteGame()
        WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.XPATH, "//button[@class='css-de05nr e19owgy710']"))).click()

        memory_test = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.CLASS_NAME, 'memory-test')))

        rounds = 1
        while rounds < max_rounds + 3:
            squares = WebDriverWait(memory_test, search_time).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-lxtdud')))
            square_rows = []

            side = len(squares)**(0.5)
            side = int(side)

            for i in range(side):
                square_rows.append([])

            i = 0
            for s in squares:
                square_rows[i // side].append(s)
                i += 1

            coords = []
            active_squares = WebDriverWait(memory_test, search_time).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'active')))

            for y in range(0, side):
                for x in range(0, side):
                    if square_rows[y][x] in active_squares:
                        coords.append((x, y))

            waitUntilDeactivated(memory_test)

            if rounds < max_rounds:
                for item in coords:
                    x = item[0]
                    y = item[1]
                    square_rows[y][x].click()
            else:
                # Lose on purpose after max_rounds reached
                clicked = 0
                for y in range(side):
                    break_outer = False
                    for x in range(side):
                        if (x, y) not in coords:
                            square_rows[y][x].click()
                            clicked += 1
                        if clicked >= 3:
                            break_outer = True
                            break
                    if break_outer:
                        break

            waitUntilDeactivated(memory_test)
            sleep(1)
            rounds += 1

    def saveScore(self):
        WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Save score')]"))).click()
        print("Press enter to close the program...", end='')
        input()
        self.driver.close()

def main():
    app = Application()

if __name__ == '__main__':
    main()

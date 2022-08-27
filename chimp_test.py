from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from userdata import username, password

# Seconds for program to wait until finding web elements
search_time = 10

class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.login()
        self.playChimpTest()
        self.saveScore()

    def login(self):
        self.driver.get('https://humanbenchmark.com/login')
        username_input = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.NAME, 'username')))
        password_input = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.NAME, 'password')))

        username_input.send_keys(username)
        password_input.send_keys(password)

        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/form/p[3]/input').click()
        sleep(1)

    def muteGame(self):
        WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.CLASS_NAME, 'fa-volume-up'))).click()

    def playChimpTest(self):
        self.driver.get('https://humanbenchmark.com/tests/chimp')
        self.muteGame()
        WebDriverWait(self.driver, search_time).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='css-de05nr e19owgy710']"))).click()

        number_count = 4

        while True:
            squares = []
            for i in range(1, number_count + 1):
                s = WebDriverWait(self.driver, search_time).until(
                    EC.presence_of_element_located((By.XPATH, f"//div[@data-cellnumber='{i}']")))
                squares.append(s)
            for s in squares:
                s.click()

            # Maximum allowed score by the game is 40
            if number_count == 40:
                break

            WebDriverWait(self.driver, search_time).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Continue')]"))).click()
            number_count += 1

    def saveScore(self):
        WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Save score')]"))).click()
        print("Press enter to close the program...", end='')
        input()
        self.driver.close()

def main():
    app = Application()

if __name__ == '__main__':
    main()
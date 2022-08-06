from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from userdata import username, password

# Maximum score that bot can do
max_score = 50

# Seconds for program to wait until finding web elements
search_time = 100

class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.login()
        self.playNumberMemory()
        self.saveScore()

    def login(self):
        self.driver.get('https://humanbenchmark.com/login')
        username_input = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.NAME, 'username')))
        password_input = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.NAME, 'password')))

        username_input.send_keys(username)
        password_input.send_keys(password)

        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/form/p[3]/input').click()
        sleep(1)

    def playNumberMemory(self):
        self.driver.get('https://humanbenchmark.com/tests/number-memory')
        WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.XPATH, "//button[@class='css-de05nr e19owgy710']"))).click()

        score = 0
        while score < max_score:
            number = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.CLASS_NAME, 'big-number'))).text
            WebDriverWait(self.driver, 999999).until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))).send_keys(number)
            WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.XPATH, "//button[@class='css-de05nr e19owgy710']"))).click()
            WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.XPATH, "//button[@class='css-de05nr e19owgy710']"))).click()
            score += 1
        WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']"))).send_keys("1")
        WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.XPATH, "//button[@class='css-de05nr e19owgy710']"))).click()
        # WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.XPATH, "//button[@class='css-de05nr e19owgy710']"))).click()

    def saveScore(self):
        WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Save score')]"))).click()
        print("Press enter to close the program...", end='')
        input()
        self.driver.close()

def main():
    app = Application()

if __name__ == '__main__':
    main()
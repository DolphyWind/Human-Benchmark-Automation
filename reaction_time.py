from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from userdata import username, password

# Seconds for program to wait until finding web elements
search_time = 10

def waitForClassNameAndClick(item, name):
    while True:
        class_attr = item.get_attribute('class')
        if class_attr.split(' ')[0] == name:
            item.click()
            return

class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.login()
        self.playReactionTime()
        self.saveScore()

    def login(self):
        self.driver.get('https://humanbenchmark.com/login')
        username_input = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.NAME, 'username')))
        password_input = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.NAME, 'password')))

        username_input.send_keys(username)
        password_input.send_keys(password)

        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/form/p[3]/input').click()
        sleep(1)

    def playReactionTime(self):
        self.driver.get("https://humanbenchmark.com/tests/reactiontime")
        rounds = 0
        max_rounds = 5
        splash = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.CLASS_NAME, 'view-splash')))
        splash.click()
        waitForClassNameAndClick(splash, 'view-go')
        rounds += 1
        while rounds < max_rounds:
            waitForClassNameAndClick(splash, 'view-result')
            waitForClassNameAndClick(splash, 'view-go')
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
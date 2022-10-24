from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from userdata import username, password

# Maximum score that bot can do
max_score = 1000

# Seconds for program to wait until finding web elements
search_time = 10

class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.words = list()
        self.login()
        self.playVerbalMemory()
        self.saveScore()

    def login(self):
        self.driver.get('https://humanbenchmark.com/login')
        username_input = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.NAME, 'username')))
        password_input = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.NAME, 'password')))

        username_input.send_keys(username)
        password_input.send_keys(password)

        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div/form/p[3]/input').click()
        sleep(1)

    def playVerbalMemory(self):
        self.driver.get("https://humanbenchmark.com/tests/verbal-memory")
        WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.XPATH, "//button[@class='css-de05nr e19owgy710']"))).click()

        score = 0
        while score < max_score:
            text = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.CLASS_NAME, 'word'))).text
            seen_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'SEEN')]")
            new_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'NEW')]")

            if text in self.words:
                seen_button.click()
            else:
                self.words.append(text)
                new_button.click()
            score += 1

        counter = 3
        while counter != 0:
            text = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.CLASS_NAME, 'word'))).text
            seen_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'SEEN')]")
            new_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'NEW')]")

            if text in self.words:
                new_button.click()
            else:
                self.words.append(text)
                seen_button.click()
            counter -= 1

    def saveScore(self):
        WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Save score')]"))).click()
        print("Press enter to close the program...", end='')
        input()
        self.driver.close()

def main():
    app = Application()

if __name__ == '__main__':
    main()
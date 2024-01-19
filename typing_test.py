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

class Application:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.login()
        self.playTypingTest()
        self.saveScore()

    def login(self):
        self.driver.get('https://humanbenchmark.com/login')
        username_input = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.NAME, 'username')))
        password_input = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.NAME, 'password')))

        username_input.send_keys(username)
        password_input.send_keys(password)

        self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/div/div/form/p[3]/input').click()
        sleep(1)

    def playTypingTest(self):
        self.driver.get("https://humanbenchmark.com/tests/typing")
        letters = WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.CLASS_NAME, 'letters')))
        text = letters.text
        letters.send_keys(text)

    def saveScore(self):
        WebDriverWait(self.driver, search_time).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Save score')]"))).click()
        print("Press enter to close the program...", end='')
        input()
        self.driver.close()


def main():
    app = Application()

if __name__ == '__main__':
    main()

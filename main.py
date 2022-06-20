import sys
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By


def wait():
    time.sleep(random.randint(3,5))
# returns if the attend button is present
def EventIsOpen(browser):
    isPresent = browser.find_elements(by=By.CSS_SELECTOR, value='#main > div.sticky.bottom-0.bg-white.w-full.py-5.z-10.px-5.xl\:px-0 > div > div > div.w-full.sm\:w-auto > div > div.flex.items-center.space-x-5.ml-5 > div:nth-child(3) > button') == []
    return isPresent

def Attend(browser):
    # Click the Attend Button
    try:
        wait()
        attendButton = browser.find_element(by=By.CSS_SELECTOR, value='#main > div.sticky.bottom-0.bg-white.w-full.py-5.z-10.px-5.xl\:px-0 > div > div > div.w-full.sm\:w-auto > div > div.flex.items-center.space-x-5.ml-5 > div:nth-child(3) > button')
        attendButton.click()
        print("Attending...")
    except:
        print('Could not find Attend Button')
    
    SignIn(browser)

def FinalSubmit(browser):
    # Wait for the screen to pop up
    time.sleep(15)

    # sometimes there's a question prompt
    try:
        questionInput = browser.find_element(by=By.XPATH, value="//input[@type='text']")
    except:
        print('No Question to be answered')

    # fill submit field
    try:
        questionInput.send_keys('ok')
    except:
        print('Could not fill out question')

    # find the submit button
    try:
        submitButton = browser.find_element(by=By.XPATH, value='//*[@id="modal"]/div/div[1]/div/form/div[4]/div/button')
        print('submit button found')
        
    except:
        print('Could not find submit')
        sys.exit()(-1)

    # Click submit button
    try:
        submitButton.click()
        print('final submit sent')
    except:
        print('could not submit')
        sys.exit()(-1)

def FillEmail(browser):
    try:
        wait()
        input = browser.find_element(by=By.ID, value='email')
        input.send_keys('email')
        print('inputing email')
    except:
        print('Could not enter email')

def FillPass(browser):
    try:
        wait()
        input = browser.find_element(by=By.ID, value='current-password')
        input.send_keys('password')       
    except:
        print('Could not fill out password')
    return input

# Signin will be prompted the first time 

def SignIn(browser):
    try:
        wait()
        signInButton = browser.find_element(by=By.XPATH, value='//*[@id="modal"]/div/div[1]/div/div/section/form/div[2]/a')
        print('found sign in button')
        browser.get(signInButton.get_attribute('href'))
        print('signing in...')
    except:
        print('Could not find sign in button')
    
    FillEmail(browser)
    FillPass(browser).submit()
    FinalSubmit(browser)

def FindEvent(browser):
    return 0    

def main():
    browser = webdriver.Safari()
    browser.get('meetuplink')
    
    if(EventIsOpen(browser)):
        Attend(browser)
    sys.exit()()


if __name__ == "__main__":
    main()

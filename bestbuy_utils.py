from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains



def best_buy_sign_in(drive, USER, PASS):
    #Sign in page
    drive.get("https://www.bestbuy.com")
    actions = ActionChains(drive)
    actions.move_by_offset(0, 200).click().perform()


    #Get to Login Prompt
    try:
        #drive.find_element_by_xpath('//button[@data-lid="hdr_signin"]').click()
        drive.find_element_by_xpath('//button[@class="lam-signIn__button btn btn-secondary"]').click()
    except:
        sleep(2)
        #drive.find_element_by_xpath('//button[@data-lid="hdr_signin"]').click()
        drive.find_element_by_xpath('//button[@class="lam-signIn__button btn btn-secondary"]').click()
    
    sleep(3)
    
    #Enter Details
    drive.find_element_by_xpath('//input[@type="email"]').send_keys(USER)
    drive.find_element_by_xpath('//input[@type="password"]').send_keys(PASS)
    
    #Signin Request
    drive.find_element_by_xpath('//button[@type="submit"]').click()
    print("Signed In!")

    return True

def best_buy_get_item(drive, link):
    
    #Go to product page
    drive.get(link)
    
    #Add to cart
    drive.find_element_by_xpath('//div[@class="fulfillment-add-to-cart-button"]').click()
    
    #Go to fulfillment page
    drive.get("https://www.bestbuy.com/checkout/r/fast-track")
    
    #Place order
    drive.find_element_by_xpath('//button[starts-with (@data-track, "Place")]').click()
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import bestbuy_utils as bbu

BEST_BUY_X = "https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324"
BEST_BUY_S = "https://www.bestbuy.com/site/microsoft-xbox-series-s-512-gb-all-digital-console-disc-free-gaming-white/6430277.p?skuId=6430277"

SIGNED_IN = False

if __name__ == "__main__":
    #Load Selenium Session
    driver = webdriver.Chrome(ChromeDriverManager().install())

    if not SIGNED_IN:
        user = input("Enter best buy email")
        password = input("Enter best buy password")
        bbu.best_buy_sign_in(driver, user, password)
        SIGNED_IN = True

    while(True):
        answer = input("Enter 'START' to begin")
        if answer=="START":
            bbu.best_buy_get_item(driver,BEST_BUY_X)
            break




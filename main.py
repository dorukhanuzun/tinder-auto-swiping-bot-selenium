from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

FACEBOOK_EMAIL = "your-email"
FACEBOOK_PASSWORD = "your password"

chrome_driver_path = "/Users/dorukhanuzun/chrome-driver/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://tinder.com/")

time.sleep(4)
login_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login_button.click()

time.sleep(4)
facebook_login_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_login_button.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element_by_name("email")
email.send_keys(FACEBOOK_EMAIL)

password = driver.find_element_by_name("pass")
password.send_keys(FACEBOOK_PASSWORD)
password.send_keys(Keys.ENTER)
driver.switch_to.window(base_window)

time.sleep(4)

allow_location = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location.click()
time.sleep(2)

allow_cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
allow_cookies.click()
time.sleep(2)

notification_not_interested = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notification_not_interested.click()

for n in range(100):
    time.sleep(5)
    try:
        like_button = driver.find_element_by_xpath(
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            no_thanks_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')
            no_thanks_button.click()
        except NoSuchElementException:
            try:
                home_screen_not_interested = driver.find_element_by_xpath(
                        '//*[@id="modal-manager"]/div/div/div[2]/button[2]')
                home_screen_not_interested.click()
            except NoSuchElementException:
                try:
                    maybe_later = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div[3]/button[2]')
                    maybe_later.click()
                except NoSuchElementException:
                    match_popup = driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[4]/button')
                    match_popup.click()
driver.quit()











from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# # driver.find_element(By.CSS_SELECTOR, "#nav-link-accountList-nav-line-1").movetoElement()
# driver.find_element(By.CSS_SELECTOR, "a[href*='register?']").click()
#
# sleep(3)
# driver.find_element(By.CSS_SELECTOR, ".nav-action-inner").click()
driver.find_element(By.CSS_SELECTOR, "i[aria-label='Amazon']")
driver.find_element(By.XPATH, "//h1[contains(text(), 'Create account')]")
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")
driver.find_element(By.CSS_SELECTOR, "input#ap_email")
driver.find_element(By.CSS_SELECTOR, "input#ap_password")
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")
driver.find_element(By.CSS_SELECTOR, "input#continue")
driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "a[href*='notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")

sleep(4)


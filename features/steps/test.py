from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


#get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com')

# click on cart
driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']").click()
sleep(4)

actual_text = driver.find_element(By.XPATH, "//h1[contains(text(), 'Your cart is empty')]").text
assert 'Your cart is empty' in actual_text, f"Error! Text Your cart is empty not found in {actual_text}"
print('Test case passed')

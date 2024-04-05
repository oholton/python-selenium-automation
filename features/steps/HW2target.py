from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
driver.find_element(By.XPATH, "//span[contains(@class, 'ListItemText') and text()='Sign in']").click()
sleep(5)

#verification

actual_text = driver.find_element(By.XPATH, "//span[contains(text(), 'Sign into your Target account')]").text
assert 'Sign into your Target account' in actual_text, f"Error! Text Sign into your Target account not found in {actual_text}"

driver.find_element(By.ID, 'login')
sleep(5)
print('Test case passed')







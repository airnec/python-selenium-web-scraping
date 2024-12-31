from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

num_of_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a").text
print(num_of_articles)

driver.quit()
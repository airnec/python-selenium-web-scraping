from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

upcoming_events = {}
unordered_list = driver.find_elements(By.CLASS_NAME, "event-widget ul li")
for element in unordered_list:
    event = {
        "time": element.text.split()[0],
        "name": element.text.split()[1] + " " + element.text.split()[2]
    }
    upcoming_events[unordered_list.index(element)] = event

for key in upcoming_events:
    print(key, upcoming_events[key])

driver.quit()
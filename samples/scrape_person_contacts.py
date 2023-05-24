import os
from linkedin_scraper import Person, actions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome("./chromedriver", options=chrome_options)
driver = webdriver.Chrome("./chromedriver")

email = os.getenv("hengleon92@gmail.com")
password = os.getenv("2301123Leon")
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://my.linkedin.com/in/kien-leong-heng-007223156", contacts=[], driver=driver)

print("Person: " + person.name)
print("Person contacts: ")

for contact in person.contacts:
	print("Contact: " + contact.name + " - " + contact.occupation + " -> " + contact.url)

import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
driver = webdriver.Firefox(options=options, executable_path="C:\Users\szege\OneDrive\Asztali gép\geckodriver\geckodriver")
driver.get("http://127.0.0.1:5500/noi.html")
time.sleep(3)
driver.save_screenshot("noi.png")
elem = driver.find_element("link text", "Férfi")
elem.click()
driver.save_screenshot("ffi.png")
time.sleep(3)
"""from datetime import datetime

D = str(datetime.now().date())
t1 = datetime.strptime(' '.join([D, '12:03:00']), '%Y-%m-%d %H:%M:%S')

t2 = datetime.now()
e = t2 - t1
print(type(e.total_seconds()))"""
import time
from selenium import webdriver

driver = webdriver.Firefox(executable_path="/u/22/koponel4/unix/geckodriver")
driver.get("file:///u/22/koponel4/unix/Documents/Workspace/tts-docker/html-2kierros/kello/kello_malli.html")

clockElem = driver.find_element_by_tag_name('h1')
time.sleep(1)
color = clockElem.value_of_css_property("color")
print(color, type(color))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import datetime
import random
import pandas as pd
import os
import time
from selenium.common.exceptions import (NoSuchElementException, StaleElementReferenceException, TimeoutException)
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options


user_agent = ''

# Create Chrome options object
options = Options()
options.add_argument(f'user-agent={user_agent}')

# Add arguments to Chrome options
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--disable-infobars')
options.add_argument('--mute-audio')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-notifications')
options.add_argument('--disable-translate')
options.add_argument('--disable-logging')
options.add_argument('--disable-default-apps')
options.add_argument('--disable-background-timer-throttling')
options.add_argument('--disable-backgrounding-occluded-windows')
options.add_argument('--disable-breakpad')
options.add_argument('--disable-component-extensions-with-background-pages')
options.add_argument('--disable-features=TranslateUI')
options.add_argument('--disable-hang-monitor')
options.add_argument('--disable-ipc-flooding-protection')
options.add_argument('--disable-prompt-on-repost')
options.add_argument('--disable-renderer-backgrounding')
options.add_argument('--disable-sync')
options.add_argument('--disable-web-resources')
options.add_argument('--enable-automation')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--log-level=3')
options.add_argument('--test-type=webdriver')
options.add_argument('--user-data-dir=/tmp/user-data')
options.add_argument('--v=99')

# Add experimental options
options.add_experimental_option('prefs', {
    'profile.managed_default_content_settings.images': 2,
    'profile.managed_default_content_settings.stylesheets': 2,
    'profile.managed_default_content_settings.plugins': 2,
    'profile.managed_default_content_settings.popups': 2,
    'profile.managed_default_content_settings.geolocation': 2,
    'profile.managed_default_content_settings.notifications': 2,
    'profile.managed_default_content_settings.automatic_downloads': 1,
    'profile.managed_default_content_settings.fullscreen': 2,
    'profile.managed_default_content_settings.mouselock': 2,
    'profile.managed_default_content_settings.pointerLock': 2,
    'profile.managed_default_content_settings.webusb': 2,
    'profile.managed_default_content_settings.webxr': 2,
    'profile.default_content_setting_values.media_stream_mic': 2,
    'profile.default_content_setting_values.media_stream_camera': 2,
})
# Start Chrome with the custom user-agent string
driver = webdriver.Chrome(options=options)

# Navigate to a website and do something
driver.get('https://web.cvent.com/hub/events/9ea99a95-3d0e-4a3b-bbca-0e974c014279/attendees')



name = []
title = []
employer = []

sleep_time = random.uniform(0.5, 2) # Changed range to match reduced pause time

# Get the initial height of the page
last_height = driver.execute_script("return document.body.scrollHeight")
names = driver.find_elements(By.XPATH, '//button[@class="css-1vmwjg"]')
time.sleep(sleep_time)
print("Number of names:", len(names)) # Prints the number of names found

# Scroll through each name element
for named in names:   
    name.append(named.text)

# Get all the title and employer elements
titles = driver.find_elements(By.XPATH, '//div[@class="css-xajf60"]/div')

# Scroll through each title and employer element
for t in titles:
    # Split the text into title and employer
    title_and_employer = t.text.split(",")
    if len(title_and_employer) == 2:
        title.append(title_and_employer[0].strip())
        employer.append(title_and_employer[1].strip())
    else:
        title.append(t.text.strip())
        employer.append("")
        time.sleep(sleep_time)

driver.quit()

df = pd.DataFrame(zip(name, title,employer), columns=['Name', 'Title','Employer'])
df.to_csv(r'C:\Users\Mauz Khan\Desktop\Cvent\Higher Education Leader Administrator.csv', index=False)
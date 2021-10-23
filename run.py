#!/usr/bin/env python3
"""
A script for creating ads.
"""
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def chrome_options():
    """
        Sets chrome options for Selenium. Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_prefs = {}
    chrome_prefs['profile.managed_default_content_settings'] = {
        'images': 2
    }
    chrome_options.experimental_options['prefs'] = chrome_prefs
    return chrome_options

def main():
    """
        Do the work.  This example shows how to change the browser location data.
    """
    url = 'https://www.mapdevelopers.com/what-country-am-i-in.php'
    driver = webdriver.Chrome(options=chrome_options())
    driver.maximize_window()
    # Grant permission to location data
    driver.execute_cdp_cmd(
        'Browser.grantPermissions',
        {
            'origin': url,
            'permissions': ['geolocation']
        },
    )
    # Set the location data
    driver.execute_cdp_cmd('Emulation.setGeolocationOverride', {
        'latitude': 30.013056,
        'longitude': 31.208853,
        'accuracy': 100
    })
    driver.get(url)
    sleep(5)
    country = driver.find_element(By.ID, 'display_country').text
    print(country)
    driver.quit()

if __name__ == "__main__":
    """
        Execute from command line
    """
    main()

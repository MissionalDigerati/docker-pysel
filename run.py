#!/usr/bin/env python3
"""
A script for creating ads.
"""
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

def chrome_options():
    """
        Sets chrome options for Selenium. Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

def main():
    """
        Create an ad.
    """
    driver = webdriver.Chrome(options=chrome_options())
    driver.set_window_size(1120, 550)
    driver.get("https://duckduckgo.com/")
    driver.find_element(By.ID, 'search_form_input_homepage').send_keys("realpython")
    driver.find_element(By.ID, 'search_button_homepage').click()
    print(driver.current_url)
    driver.quit()


if __name__ == "__main__":
    """
        Execute from command line
    """
    main()

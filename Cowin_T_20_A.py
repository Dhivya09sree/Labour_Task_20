from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


class Cowin:
    def __init__(self):
        self.driver = None
        self.wait_timeout = 15


 # Initialize the ChromeDriver
    def initialize_driver(self):
        service = Service(ChromeDriverManager().install())
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome(service=service)

# OPen a website
    def open_website(self, url):
        self.driver.get(url)

# Maximize the browser window
    def maximize_window(self):
        self.driver.maximize_window()

# Wait for an element to be clickable
    def click(self, locator, timeout=None):
        timeout = timeout or self.wait_timeout
        return WebDriverWait(self.driver, timeout).until(
        EC.element_to_be_clickable(locator))


    def get_latest_window_handle(self):
      return self.driver.window_handles[-1]


    def switch_to_window(self, window_handle):
     self.driver.switch_to.window(window_handle)


# Click on the "FAQ" link
    def click_faq_link(self):
        faq_link_locator = (By.LINK_TEXT, "FAQ")
        faq_link = self.click(faq_link_locator)
        faq_link.click()

# Click on the "Partners" link
    def click_partners_link(self):
        partners_link_locator = (By.XPATH, '//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a')
        partners_link = self.click(partners_link_locator)
        partners_link.click()

# Fetch and display opened window IDs
    def display_opened_windows(self):
        window_handles = self.driver.window_handles
        print("Opened Windows ID:")
        for handle in window_handles:
            print(handle)

    def close_current_window(self):
        self.driver.close()

# Create an object of the class
cowin = Cowin()

# Initialize the browser
cowin.initialize_driver()

# Open the CoWIN website
cowin.open_website("https://www.cowin.gov.in/")

# Maximize the browser window
cowin.maximize_window()

# Store the main window handle
main_window_handle = cowin.driver.current_window_handle
print("Main Window Handle:", main_window_handle)

# Click on the "FAQ" link
cowin.click_faq_link()
time.sleep(3)

# Store the FAQ window handle
faq_window_handle = cowin.get_latest_window_handle()
print("FAQ Window Handle:", faq_window_handle)

# Switch back to the main window
cowin.switch_to_window(main_window_handle)

# Click on the "Partners" link
cowin.click_partners_link()
time.sleep(3)

# Store the Partners window handle
partners_window_handle = cowin.get_latest_window_handle()
print("Partners Window Handle:", partners_window_handle)

# Close the Partners window
cowin.switch_to_window(partners_window_handle)
cowin.close_current_window()
time.sleep(3)

# Switch to the FAQ window and close it
cowin.switch_to_window(faq_window_handle)
cowin.close_current_window()
time.sleep(3)

# Switch back to the main window and close it
cowin.switch_to_window(main_window_handle)
cowin.close_current_window()
time.sleep(3)














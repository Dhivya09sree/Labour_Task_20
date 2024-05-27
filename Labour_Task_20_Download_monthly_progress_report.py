from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import requests
import os

class Labour:
    def __init__(self):
        self.driver = None
        self.wait_timeout = 15

    # Initialize the ChromeDriver
    def initialize_driver(self):
        service = Service(ChromeDriverManager().install())
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, self.wait_timeout)

    # Open a website
    def open_website(self, url):
        self.driver.get(url)

    # Maximize the browser window
    def maximize_window(self):
        self.driver.maximize_window()

    # Wait for an element to be clickable
    def click(self, locator, timeout=None):
        timeout = timeout or self.wait_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click_monthly_progress_report(self):
        # Go to the "Documents" menu
        time.sleep(2)
        documents_menu = self.wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[contains(text(), "Documents")])[3]')))
        time.sleep(3)
        ActionChains(self.driver).move_to_element(documents_menu).perform()

        #documents_menu.click()

        time.sleep(5)

        # Click the "Monthly Progress Report" link
        monthly_report_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Monthly Progress Report")]')))
        monthly_report_link.click()

        # download the "Monthly Progress Report" link
    def download_monthly_progress_report(self):

       # Find all the monthly progress reports
       report_links = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr/td[2]/a')))

       for index, link in enumerate(report_links, start=1):
           file_url = link.get_attribute('href')

           # Download  all the monthly progress report
           report_response = requests.get(file_url)
           with open(os.path.join(os.path.expanduser('~'), 'Downloads', f'Monthly_Progress_Report_{index}.pdf'),
                     'wb') as file:
               file.write(report_response.content)

           print(f"Monthly Progress Report {index} downloaded successfully.")

    print("Monthly Progress Report downloaded successfully.")

# Create the object
Labourobj = Labour()

# Initialize the browser
Labourobj.initialize_driver()
# Open the website
Labourobj.open_website('https://labour.gov.in/')

Labourobj.maximize_window()

# Download the monthly progress report
Labourobj.click_monthly_progress_report()

Labourobj.download_monthly_progress_report()
time.sleep(5)

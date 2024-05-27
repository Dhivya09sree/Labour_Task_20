from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import os


class Labour_Photos_download:
    def __init__(self):
        self.driver = None
        self.wait_timeout = 15
        self.photo_folder = r"C:\Users\dhivy\OneDrive\Desktop\Photo_Gallery"
        if not os.path.exists(self.photo_folder):
            os.makedirs(self.photo_folder)

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

    # Navigate to the "Media" menu and then to "Photo Gallery
    def open_media_photo_gallery(self):
        media_menu = self.driver.find_element(By.LINK_TEXT, "Media")
        media_menu.click()

        all_press_release = self.driver.find_element(By.LINK_TEXT, "Click for more info of Press Releases")
        all_press_release.click()

        photo_gallery_menu = self.driver.find_element(By.LINK_TEXT, "Photo Gallery")
        photo_gallery_menu.click()
        time.sleep(5)  # Wait for the page to load

    # Download the first 10 photos
    def download_first_10_photos(self):
        # Wait for the photo gallery images to be present
        photos = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#fontSize > div > div > div.aboutmainContainer > div.aboutRightContainer > div:nth-child(1) > div > div > div.scroll-table1 > div.scroll-table img")))[:10]
        for index, photo in enumerate(photos):
            photo_url = photo.get_attribute('src')
            if photo_url:
                photo_response = requests.get(photo_url)
                with open(os.path.join(self.photo_folder, f"photo_{index + 1}.jpg"), 'wb') as file:
                    file.write(photo_response.content)
                print(f"Downloaded photo {index + 1}")


        print("Photos downloaded successfully.")


# Create the object
Labourobj = Labour_Photos_download()

# Initialize the browser
Labourobj.initialize_driver()
# Open the website
Labourobj.open_website('https://labour.gov.in/')

Labourobj.maximize_window()

Labourobj.open_media_photo_gallery()

Labourobj.download_first_10_photos()

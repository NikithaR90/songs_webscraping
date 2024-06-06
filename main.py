from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Import the By class
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the URL
driver.get('https://soundcloud.com/')

# Wait for JavaScript to load content
time.sleep(5)  # Adjust as necessary

# Find all elements by class name
songs = driver.find_elements(By.CSS_SELECTOR, 'a.playableTile__heading')  # Updated method call
song_titles = [song.text for song in songs if song.text != '']  # Collect non-empty song titles

# Clean up
driver.quit()

# Save to CSV
csv_file_path = 'songs.csv'
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Song Title'])  # Writing the header
    for title in song_titles:
        writer.writerow([title])  # Writing song titles

print(f"Data has been written to '{csv_file_path}'")
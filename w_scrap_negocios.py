
# Web Scraping of a Determined by topic
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re  # Import the re module for regular expressions

# Paths
ad1 = "https://www.science.org/doi/10.1126/science.adg2833"
ad2 = "https://www.robotscrate.com/"
determined_web = ad1
chrome_driver_path = 'C:/Users/user/Documents/LEGAL_SCR/Chrome_driver/chromedriver.exe'

# Initialize the ChromeDriver with SERVICE V116
service = webdriver.chrome.service.Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(determined_web)  # Open Site

html = driver.page_source  # Extract HTML

soup = BeautifulSoup(html, 'html.parser')  # Use BeautifulSoup to parse HTML

# Find and extract specific information related to divorce using regular expressions
text_to_get = []

# You can customize this regular expression to match the specific content related to divorce
# For example, if the information you want is in <p> tags with class "divorce-info", you can use:
# regex_pattern = r'<p class="divorce-info">(.+?)</p>'
regex_pattern = r'(economia|negocios|inversion)'  # Example pattern, adjust as needed

for paragraph in soup.find_all('p'):
    paragraph_text = paragraph.get_text()
    if re.search(regex_pattern, paragraph_text, re.IGNORECASE):
        text_to_get.append(paragraph_text)

# Print the extracted information related to divorce
for info in text_to_get:
    print(info)

# Close the browser window
driver.quit()

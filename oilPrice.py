from bs4 import BeautifulSoup as soup
from playwright.sync_api import sync_playwright
from songline import Sendline


url = 'https://www.shell.co.th/th_th/customer/fuels-and-lubricants/fuels/fuel-price.html'
token = '4ED99HkYOoqVUEdd6SPN4OOegI3S7zqu5ZYYwi5QstA'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)
    
    # Wait for the content to load
    page.wait_for_load_state('networkidle')
    
    # Get the page content
    html = page.content()
    
    
    browser.close()

data = soup(html, 'html.parser')


price = data.tbody.find_all('tr')

lineMsg = ''

for p in price[1:]:
    nameAndPrice = p.find_all('td')

    oil_name = nameAndPrice[0].text
    price_name = nameAndPrice[1].text
    msg = "{} {}".format(oil_name, price_name)
    
    lineMsg += msg + "\n"


# initiate line bot to send message in line notify
line_bot = Sendline(token)

line_bot.sendtext(lineMsg)
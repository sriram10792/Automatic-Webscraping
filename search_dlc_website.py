import time
import base64
from PIL import Image
from io import BytesIO
from io import StringIO
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#Test word. To be extracted from efile 
word='CPL40AUP50 400'

#Open firefox
browser = webdriver.Firefox()

#Got to the website
browser.get('https://www.designlights.org/search/')


#Find the SEARCH bar and pass the Search term 
elem = browser.find_element_by_name('search')
elem.send_keys(word + Keys.RETURN)



#Wait till the results card load

element = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".details")))


#Print the number of results found in the search
elements1 = browser.find_elements_by_class_name('result')
count=elements1[0].text

#Search results bar image
print(count)
search_count=browser.find_elements_by_class_name('result')[0].screenshot_as_png
search_count_image=Image.open(BytesIO(search_count))
search_count_image.save('searchbar.png')


#To save screenshot of the result - Wattage
watt_result = browser.find_elements_by_class_name('bottom-content')[0].screenshot_as_png
watt_image=Image.open(BytesIO(watt_result))
watt_image.save('watt.png')


WebDriverWait(browser,20)



#To print the result of each product found in the result

result_cards_count= len(browser.find_elements_by_class_name('product-card'))
for i in range (result_cards_count):
    result_count = browser.find_elements_by_class_name('product-card')[i].screenshot_as_png
    result_image = Image.open(BytesIO(result_count))
    result_image.save('screenshot'+str(i+1)+'.png')
    
       


#To get the screenshot of the result web page        
browser.save_screenshot('dlc.png')



# To close the Browser

browser.quit()
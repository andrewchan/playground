from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
browser = Firefox(options=opts)
browser.get('https://bandcamp.com')
#browser.find_element_by_class_name('play-btn').click()
tracks = browser.find_elements_by_class_name('discover-item')
#print(len(tracks))
#tracks[2].click()
discover_results = browser.find_element_by_class_name('discover-result')
print(tracks[2].text)
browser.close()
quit()    
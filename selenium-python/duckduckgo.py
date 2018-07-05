from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
#opts.set_headless()
browser = Firefox(options=opts)
browser.get("https://duckduckgo.com")
search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('python tutorial')
search_btn = browser.find_element_by_id('search_button_homepage')
search_btn.click()
browser.close()
quit()
#search_form.submit()
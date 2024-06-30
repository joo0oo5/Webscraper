from selenium import webdriver

url = 'https://results.eci.gov.in/'
browser = webdriver.Chrome()
browser.get(url)

browser.find_element("xpath",'/html/body/main/div[2]/section/div/div/div[1]/div/a').click()


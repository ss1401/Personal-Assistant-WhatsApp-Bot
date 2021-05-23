from selenium import webdriver
import time
import pyodbc


options = webdriver.ChromeOptions()
chrome_browser = webdriver.Chrome(
    executable_path=r'chromedriver.exe')
chrome_browser.get('https://web.whatsapp.com/')


def new_chat(user_name):
    print(user_name)
    new_search = chrome_browser.find_elements_by_xpath('//div[@class = "SgIJV"]')
    for x in new_search:
        x.click()
    new_user = chrome_browser.find_elements_by_xpath('//div[@class = "_2_1wd copyable-text selectable-text"]')
    for x in new_user:
        x.send_keys(user_name)



#def text_now(send_message):
time.sleep(10)
print('Scanning time is up')

user_name_list = ['aadi','Janhavi Mhatre','Sahana Shetty','Rakshita Danee','Yash Rajeee']
#send_message="Good morning!, Meet Link for Lecture: https://meet.google.com/rpv-dfwe-ffw "


for user_name in user_name_list:
    new_chat(user_name)
    time.sleep(3)
    current_user = []
    a=0
    user = chrome_browser.find_elements_by_xpath('//span[@title = "{}"]'.format(user_name))
    for x in user:
        current_user.append(x)
        a=a+1
    current_user[a-1].click()
    message_box = chrome_browser.find_elements_by_xpath('//div[@class = "_2_1wd copyable-text selectable-text"]')
    for x in message_box:
        x.send_keys('{}'.format(send_message))
    send_button = chrome_browser.find_elements_by_xpath('//button[@class = "_1E0Oz"]')
    for x in send_button:
        x.click()



print('End of code')



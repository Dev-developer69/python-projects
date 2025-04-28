# for posting in facebook
# importing selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# importing time
import time

# using driver
driver= webdriver.Chrome()

# attaching link
driver.get('https://www.facebook.com')
# maximizing the window
driver.maximize_window()
time.sleep(5)

# finding id element on page and filling the id
try:
    emailelement= driver.find_element(By.XPATH,(".//*[@id='email']"))
    emailelement.send_keys('Username')
    time.sleep(2)
except:
    print('login field not found')

# finding password field and filling of password
try:
    passelement= driver.find_element(By.XPATH,(".//*[@id='pass']"))
    passelement.send_keys('Password')
    time.sleep(2)
except:
    print("passworld field not found")

# login using the id and pass
try:
    elem= driver.find_element(By.XPATH,"//button[@name='login']")
    elem.click()
    time.sleep(10)
except:
    print('unable to find login button ')

# try:
#     popup_close_button = driver.find_element(By.XPATH, '//button[contains(text(), "Block")]')  # Example for "Not Now" button
#     popup_close_button.click()
#     print("Popup closed.")
# except:
#         print("No popup appeared.")
#         time.sleep(20)

#   going to the home page for locating post field
try:
    elem1= driver.find_element(By.XPATH,"//span[@class='x1n2onr6']")
    elem1.click()
    time.sleep(10)
except:
    print("unable to find the home page")

# clicking the post to open the pop up window for writing of the post's content
try:
    status_prompt = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//a[@aria-current='page']")))
    driver.execute_script("arguments[0].click();", status_prompt)
    time.sleep(2)
    post_prompt = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//div[@class ='x1i10hfl x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 xmjcpbm x107yiy2 xv8uw2v x1tfwpuw x2g32xy x78zum5 x1q0g3np x1iyjqo2 x1nhvcw1 x1n2onr6 xt7dq6l x1ba4aug x1y1aw1k xn6708d xwib8y2 x1ye3gou']")))
    driver.execute_script("arguments[0].click();", post_prompt)
    time.sleep(2)
except:
    print('wait error / reload error')

# writing of the content of the post
try:
    status_text_area = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']")))
    driver.switch_to.active_element.send_keys("Hello I am being automated !")
except:
    print('post write error')

# posting the content to facebook
try:
    post_button = driver.find_element(By.XPATH, "//span[text()='Post']")
    post_button.click()
    time.sleep(10)
    print('Successfully posted')
except:
    print('post button error')

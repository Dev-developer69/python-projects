# importing selenium for automation
from selenium import webdriver

# used for locating elements
from selenium.webdriver.common.by import By

# used for dynamic waiting
import time

# using chrome
driver= webdriver.Chrome()

# link of the form
driver.get('https://forms.gle/cntJiTYZHhbjPxss7')
# used for waiting for page element to reload
time.sleep(4)
# maximizing the window
driver.maximize_window()
time.sleep(2)

# try and except method if any error occurs then rest of code will run while not returning error

# Name field
try:
    # field where data is to be inputted
    name= driver.find_element(By.XPATH,'//input[@type="text"] ')
    # data which is to be inputted
    name.send_keys('Devansh Maheshwari')
    time.sleep(2)
except:
    # output if any error occurred
    print("name not found")
# rest same as above

# Looking field
try:
    name= driver.find_element(By.XPATH,'(//div[@class="Xb9hP"]//input)[2] ')
    name.send_keys('Frontend developer')
    time.sleep(2)
except:
    print("looking for not found")

# Email field
try:
    name= driver.find_element(By.XPATH,'(//div[@class="Xb9hP"]//input)[3] ')
    name.send_keys('devansh@gmail.com')
    time.sleep(2)
except:
    print("Email not found")

# Number field
try:
    name= driver.find_element(By.XPATH,'(//div[@class="Xb9hP"]//input)[4] ')
    name.send_keys('6396500641')
    time.sleep(2)
except:
    print("phone number not found")

# College Name field
try:
    name= driver.find_element(By.XPATH,'(//div[@class="Xb9hP"]//input)[5] ')
    name.send_keys('Rajshree institute of management and technology ')
    time.sleep(2)
except:
    print("college not found")

# Certificates
try:
    name= driver.find_element(By.XPATH,'(//div[@class="Xb9hP"]//input)[6] ')
    name.send_keys('Python ')
    # time.sleep(2)
except:
    print("Certificates not found")

# Certificates
try:
    name= driver.find_element(By.XPATH,'(//div[@class="Xb9hP"]//input)[6] ')
    name.send_keys(' C ')
except:
    print("Certificates not found")

# Certificates
try:
    name= driver.find_element(By.XPATH,'(//div[@class="Xb9hP"]//input)[6] ')
    name.send_keys(' Web designing ')
    time.sleep(2)
except:
    print("Certificates not found")

# Skills field
try:
    name= driver.find_element(By.XPATH,'(//textarea[@class="KHxj8b tL9Q4c"]) ')
    name.send_keys('Python ')
    time.sleep(2)
except:
    print("Skills not found")

# Skills field
try:
    name= driver.find_element(By.XPATH,'(//textarea[@class="KHxj8b tL9Q4c"]) ')
    name.send_keys('HTML ')
except:
    print("Skills not found")

# Skills field
try:
    name= driver.find_element(By.XPATH,'(//textarea[@class="KHxj8b tL9Q4c"]) ')
    name.send_keys('CSS ')
except:
    print("Skills not found")

# Internship field
try:
    name= driver.find_element(By.XPATH,'(//div[@class="Xb9hP"]//input)[7] ')
    name.send_keys('Python from TUTEDUDE')
    time.sleep(2)
except:
    print("Certificates not found")

# Submit button
try:
    name= driver.find_element(By.XPATH,'(//span[@class="l4V7wb Fxmcue"]) ')
    name.click()
    time.sleep(3)
except:
    print("Submit button not found")

time.sleep(3)



import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

YOUR_USERNAME = ""
YOUR_EMAIL = ""
YOUR_PASSWORD = ""
YOUR_ISP = ""
YOUR_LOCATION = ""

driver_path = r"D:\Development\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=driver_path)

driver = webdriver.Chrome(service=service)

driver.get(url="https://www.highspeedinternet.com/tools/speed-test")

time.sleep(3)

actions = ActionChains(driver)
actions.send_keys(Keys.PAGE_DOWN).perform()
## MAY HAVE TO ADJUST THE SCROLL AS THE WEBSITE IS ALWAYS CHANGING

try:
    test = driver.find_element(By.XPATH, value="//button[@class='start-speed-test']")
    test.click()
    time.sleep(3)
    X = driver.find_element(By.XPATH, value='//*[@id="onetrust-close-btn-container"]/button')
    X.click()

    time.sleep(40)
except Exception as e:
    print(f"Button error: {e}")


download = (driver.find_element(By.XPATH, value='//*[@id="speed-test-banner"]/div[1]/div/div/div/div[2]/div[2]/div/div[1]/strong')).text
time.sleep(4)
upload = (driver.find_element(By.XPATH, value='//*[@id="speed-test-banner"]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/strong')).text
time.sleep(4)
ping = (driver.find_element(By.XPATH, value='//*[@id="speed-test-banner"]/div[1]/div/div/div/div[2]/div[2]/div/div[3]/strong')).text

dnld_value = float((download.split(" "))[0])
upld_value = float((upload.split(" "))[0])
png_vlaue = float((ping.split(" "))[0])

if dnld_value < 10 or upld_value < 18:
    tweet = (f"Hey @{YOUR_ISP}, why is my internet speed {dnld_value}down/{upld_value}up\n"
             f"When I pay for 10down/18up in {YOUR_LOCATION}")

if png_vlaue > 80:
    ping_tweet = f"The ping is {png_vlaue}ms which is diabolical"


# SECOND STEP

driver.get(url="https://x.com/")

time.sleep(10)
actions.send_keys(Keys.PAGE_DOWN).perform()


### SIGN IN
try:
    time.sleep(3)
    sign_in = driver.find_element(By.XPATH, value="//span[contains(text(),'Sign in')]")
    sign_in.click()
except Exception as e:
    print(f"sign in error: {e}")

## EMAIL
try:
    time.sleep(20)
    email = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
    email.send_keys(f"{YOUR_USERNAME}")

except Exception as f:
    print(f"mail error: {f}")


## NEXT
try:
    nxt = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
    nxt.click()
    time.sleep(20)
except Exception as h:
    print(f"nxt error: {h}")


## MAIL II
try:
    time.sleep(20)
    again_mail = driver.find_element(By.XPATH, value="//input[@name='text']")
    again_mail.send_keys(f"{YOUR_EMAIL}")
    alt_next = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
    alt_next.click()
except Exception as i:
    print(f"mail II error: {i}")


## PASSWORD
try:
    time.sleep(5)
    password = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys(f"{YOUR_PASSWORD}")

except Exception as g:
    print(f"password error: {g}")


# LOG IN
login = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span')
login.click()
time.sleep(20)

## POSTING
post_box = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
post_box.send_keys(f"{tweet}\n{ping_tweet}")

## POST
time.sleep(5)
post_button = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
print("post button located")
## UNCOMMENT below to post
# post_button.click()

input("Press Enter to close...")
driver.quit()







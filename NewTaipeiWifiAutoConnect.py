import logging
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# 設定日誌
logging.basicConfig(level=logging.DEBUG)

# 設定WebDriver路徑
geckodriver_path = r"C:\Users\liangtinglin\Documents\python\NewTaipeiWifiAutoConnect\geckodriver.exe"
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"

service = FirefoxService(executable_path=geckodriver_path)
options = webdriver.FirefoxOptions()
options.binary_location = firefox_binary_path
options.add_argument('--headless') # 如果不需要瀏覽器介面視覺化，可以使用無頭模式

# 初始化WebDriver
driver = webdriver.Firefox(service=service, options=options)

try:
     # 造訪Wi-Fi登入頁面
     driver.get("http://newtaipei.cht.com.tw/")
     
     # 等待登入按鈕可點擊，並進行點擊操作
     login_button = WebDriverWait(driver, 15).until(
         EC.element_to_be_clickable((By.XPATH, "//a[img[@alt='免費網際網路']]"))
     )
     login_button.click()
     logging.info("Login button clicked.")

     # 等待頁面出現某些元素，例如跳轉後的特定標識，這裡假設新頁面有特定的header標題
     WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), '歡迎')]"))
     )
     logging.info("Login confirmed by page transition.")

except TimeoutException:
     logging.error("Timeout during login process.")
except NoSuchElementException:
     logging.error("Required element not found.")
except Exception as e:
     logging.error(f"An error occurred: {e}")
finally:
     # 退出WebDriver
     driver.quit()
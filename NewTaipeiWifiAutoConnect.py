from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

# 設定日誌
logging.basicConfig(level=logging.DEBUG)

# 設定 WebDriver 路徑
geckodriver_path = r"C:\Users\liangtinglin\Documents\python\NewTaipeiWifiAutoConnect\geckodriver.exe"
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"

# 初始化 WebDriver
service = FirefoxService(executable_path=geckodriver_path)
options = Options()
options.binary_location = firefox_binary_path
options.add_argument('--headless')  # 使用無頭模式

driver = webdriver.Firefox(service=service, options=options)

try:
    # 造訪 Wi-Fi 登入頁面
    driver.get("http://newtaipei.cht.com.tw/")
    
    # 等待登入按鈕可點擊，並進行點擊操作
    login_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[img[@alt='免費網際網路']]"))
    )
    login_button.click()
    logging.info("Login button clicked.")
    
    # 檢查是否跳轉到 Facebook
    WebDriverWait(driver, 15).until(
        lambda d: d.current_url == "https://www.facebook.com/myntpc/"
    )
    logging.info("Successfully connected, redirected to Facebook page.")

except TimeoutException:
    logging.error("Timeout during login or redirection process.")
except Exception as e:
    logging.error(f"An error occurred: {e}")
finally:
    driver.quit()

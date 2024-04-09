import logging
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# 設定日誌級別為DEBUG來獲取詳細信息
# Set the logging level to DEBUG to get detailed information
logging.basicConfig(level=logging.DEBUG)

# 初始化Tkinter，但不顯示主窗口
# Initialize Tkinter, but do not display the main window
Tk().withdraw()

# 函數檢查文件是否存在且正確
# Function to check if the file exists and is correct
def select_file(prompt, initialdir, filetypes):
    path = askopenfilename(title=prompt, initialdir=initialdir, filetypes=filetypes)
    if path:
        return path
    else:
        logging.error("File selection cancelled.")
        exit()

# 指定geckodriver WebDriver路徑
# Specify the geckodriver WebDriver path
geckodriver_path = r"C:\Users\liangtinglin\Documents\python\newTaipei\geckodriver.exe"  # 替換為你的geckodriver的實際路徑
                                                                                  # Replace with your actual geckodriver path
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # 替換為你的Firefox瀏覽器的實際路徑
                                                                       # Replace with your actual Firefox browser path

# 檢查文件是否存在和正確
# Check if the files exist and are correct
if not os.path.isfile(geckodriver_path) or not "geckodriver.exe" in geckodriver_path:
    logging.warning("Invalid or missing geckodriver. Please select geckodriver.exe.")
    geckodriver_path = select_file("Select geckodriver.exe", "/", [("Executable", "*.exe")])

if not os.path.isfile(firefox_binary_path) or not "firefox.exe" in firefox_binary_path:
    logging.warning("Invalid or missing Firefox binary. Please select firefox.exe.")
    firefox_binary_path = select_file("Select firefox.exe", "/", [("Executable", "*.exe")])

service = FirefoxService(executable_path=geckodriver_path)

# 設置Selenium Webdriver的選項
# Set the Selenium Webdriver options
options = webdriver.FirefoxOptions()
options.add_argument('--headless')  # 無頭模式
                                    # Headless mode
options.binary_location = firefox_binary_path  # 指定Firefox二進制路徑
                                                # Specify Firefox binary path

# 使用指定的Service
# Use the specified Service
driver = webdriver.Firefox(service=service, options=options)

# 訪問Wi-Fi登錄頁面
# Visit the Wi-Fi login page
driver.get("http://newtaipei.cht.com.tw/internet/active")

# 等待紅色按鈕出現
# Wait for the red button to appear
try:
    agree_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//a[img[@alt="免費網際網路"]]'))
    )
    agree_button.click()
except TimeoutException:
    logging.error("Timeout while waiting for the element.")
except Exception as e:
    logging.error(f"An error occurred: {e}")
finally:
    # 確保腳本完成後關閉驅動程序
    # Make sure to close the driver after the script is done
    driver.quit()

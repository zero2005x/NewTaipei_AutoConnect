# NewTaipeiWifiAutoConnect

# Selenium Firefox WebDriver 設定示例 - 自動連上NewTaipei WiFi的腳本
# Selenium Firefox WebDriver Setup Example - A script to connect NewTaipei WiFi automatically

## 功能介紹
## Feature Introduction

此程式碼示範了如何使用 Selenium WebDriver 配合 Firefox 瀏覽器自動化測試或自動化任務。它包含了檢查指定的 `geckodriver` 和 Firefox 二進制文件的存在與正確性，如果文件不存在或不正確，則使用 `tkinter` 的檔案選擇對話框提示用戶選擇正確的文件路徑。此外，程式碼展示了如何設置 WebDriver 以無頭模式運行，並訪問特定網頁，等待特定元素出現後進行點擊動作。

This code demonstrates how to automate tasks or testing with Selenium WebDriver using the Firefox browser. It includes checks for the existence and correctness of the specified `geckodriver` and Firefox binary files, prompting the user to select the correct file paths via a `tkinter` file dialog if the files are missing or incorrect. Additionally, the code shows how to set up the WebDriver to run in headless mode, navigate to a specific webpage, wait for a specific element to appear, and then perform a click action.

## 使用方法
## Usage

1. 確保您已安裝 Python 3 和相關套件：`selenium` 和 `tkinter`。
2. 將此程式碼保存為 `.py` 文件。
3. 根據您的系統路徑修改 `geckodriver_path` 和 `firefox_binary_path` 變數。
4. 透過終端機或命令提示字元運行程式。

1. Ensure you have Python 3 and the required packages installed: `selenium` and `tkinter`.
2. Save this code as a `.py` file.
3. Modify the `geckodriver_path` and `firefox_binary_path` variables according to your system paths.
4. Run the program via a terminal or command prompt.

## 需求
## Requirements

- Python 3
- selenium
- tkinter

## 注意事項
## Notes

- 此程式碼僅為示例，實際應用時可能需要根據具體需求進行調整。
- 使用前請確保 Firefox 瀏覽器已安裝於您的系統中。

- This code is provided as an example, and may need to be adjusted for specific needs in actual applications.
- Ensure that the Firefox browser is installed on your system before using.
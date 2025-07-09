from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # تشغيل بدون واجهة (اختياري)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://t.me/Media1DownloaderBot")  # رابط البوت أو الصفحة المطلوبة
        time.sleep(5)  # انتظار تحميل الصفحة

        # مثال: الضغط على زر معين
        button = driver.find_element(By.XPATH, '//button[contains(text(),"Start")]')
        button.click()

        time.sleep(10)  # تنفيذ أي تفاعل آخر حسب الحاجة

    except Exception as e:
        print(f"Error: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()

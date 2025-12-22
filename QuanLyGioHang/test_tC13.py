import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestTC13:
    def setup_method(self, method):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC13(self):
        self.driver.get("http://hauiproj.somee.com/Default.aspx")
        time.sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, "#HyperLink2 > li").click()
        time.sleep(2)

        self.driver.find_element(By.ID, "ContentPlaceHolder1_DataList1_Image1_0").click()
        time.sleep(2)

        # Thêm lần 1
        self.driver.find_element(By.ID, "ContentPlaceHolder1_Datalist1_btnThemVaoGio_0").click()
        time.sleep(2)

        # Thêm lần 2 (đã có trong giỏ)
        self.driver.find_element(By.ID, "ContentPlaceHolder1_Datalist1_btnThemVaoGio_0").click()
        time.sleep(2)

        # Xem giỏ
        self.driver.find_element(By.CSS_SELECTOR, "#HyperLink4 > li").click()
        time.sleep(2)

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestTC10:
    def setup_method(self, method):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC10(self):
        self.driver.get("http://hauiproj.somee.com/Default.aspx")

        cart = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#HyperLink4 > li"))
        )
        cart.click()

        message = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "ContentPlaceHolder1_gvGioHang_Label1")
            )
        )

        assert message.text == "Không có mặt hàng nào trong giỏ hàng!"

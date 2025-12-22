import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTC61:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)

    def teardown_method(self):
        self.driver.quit()

    def js_click(self, css):
        el = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css))
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", el
        )
        self.driver.execute_script("arguments[0].click();", el)

    def test_tC61(self):
        self.driver.get("http://hauiproj.somee.com/Default.aspx")
        self.driver.set_window_size(1014, 687)

        # Login
        self.wait.until(EC.element_to_be_clickable((By.ID, "LinkDN"))).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "ContentPlaceHolder1_txtTaikhoan")
            )
        ).send_keys("admin")

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtMatkhau"
        ).send_keys("1234")

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_btDangnhap"
        ).click()

        # Vào bảo trì danh mục
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#HyperLink5 > li"))
        ).click()

        # ⚠️ 3 nút này BẮT BUỘC JS click
        self.js_click(".item-data:nth-child(6) .bt-style-chucnang:nth-child(1)")
        self.js_click(".item-data:nth-child(8) .bt-style-chucnang:nth-child(1)")
        self.js_click(".item-data:nth-child(8) .bt-style-chucnang:nth-child(2)")

        # Logout
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "LinkDX"))
        ).click()

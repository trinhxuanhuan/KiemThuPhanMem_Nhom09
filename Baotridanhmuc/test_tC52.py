import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException

class TestTC52:
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 20)

    def teardown_method(self):
        self.driver.quit()

    def test_tC52(self):
        url = "http://hauiproj.somee.com/Default.aspx"

        try:
            self.driver.get(url)
        except WebDriverException:
            pytest.skip("Website không truy cập được (DNS lỗi hoặc server down)")

        # Đợi link đăng nhập xuất hiện
        try:
            self.wait.until(EC.element_to_be_clickable((By.ID, "LinkDN"))).click()
        except TimeoutException:
            pytest.skip("Trang load không thành công")

        self.wait.until(EC.visibility_of_element_located(
            (By.ID, "ContentPlaceHolder1_txtTaikhoan")
        )).send_keys("admin")

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtMatkhau"
        ).send_keys("1234")

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_btDangnhap"
        ).click()

        # Vào quản lý danh mục
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#HyperLink5 > li")
        )).click()

        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "ContentPlaceHolder1_txtID")
        )).send_keys("11")

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtTenDM"
        ).send_keys("Kính không gọng")

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_LinkButton1"
        ).click()

        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "LinkDX")
        )).click()

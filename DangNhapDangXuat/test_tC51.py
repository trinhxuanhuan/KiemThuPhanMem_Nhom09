import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTC51:

    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        self.driver.quit()

    def test_tC51(self):
        driver = self.driver
        wait = self.wait

        # Mở trang
        driver.get("http://hauiproj.somee.com/Default.aspx")
        driver.set_window_size(1086, 700)

        # LOGIN
        wait.until(EC.visibility_of_element_located((By.ID, "txtTenDangNhap"))).send_keys("admin")
        driver.find_element(By.ID, "txtMatKhau").send_keys("123456")
        driver.find_element(By.ID, "btnDangNhap").click()

        # LOGOUT
        wait.until(EC.element_to_be_clickable((By.ID, "LinkDX"))).click()

        # VERIFY LOGOUT (quay về trạng thái chưa đăng nhập)
        wait.until(EC.visibility_of_element_located((By.ID, "btnDangNhap")))

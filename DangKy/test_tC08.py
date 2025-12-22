import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTC08():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)

    def teardown_method(self, method):
        self.driver.quit()

    def scroll_to(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", element
        )

    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def test_tC08(self):
        self.driver.get("http://hauiproj.somee.com/Default.aspx")
        self.driver.set_window_size(1366, 728)

        # Mở form đăng ký
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "LinkDK"))
        ).click()

        # Tài khoản (chỉ nhập khoảng trắng – test validation)
        tk = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_txtTaiKhoan")
            )
        )
        self.scroll_to(tk)
        tk.send_keys("  ")

        # Mật khẩu
        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtMatKhau"
        ).send_keys("thuan123")

        # Họ tên
        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtHoTen"
        ).send_keys("Nguyễn Hưng Thuận")

        # Năm sinh
        namsinh = self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtNamSinh"
        )
        self.scroll_to(namsinh)
        namsinh.send_keys("2005-09-04")

        # Giới tính
        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_dllGioiTinh"
        ).click()
        self.driver.find_element(
            By.CSS_SELECTOR, "option:nth-child(1)"
        ).click()

        # Email
        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtEmail"
        ).send_keys("thuan205@gmail.com")

        # SĐT (bị che quảng cáo → scroll trước)
        sdt = self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtSdt"
        )
        self.scroll_to(sdt)
        sdt.send_keys("0963053320")

        # Địa chỉ
        diachi = self.driver.find_element(
            By.ID, "ContentPlaceHolder1_txtDiaChi"
        )
        self.scroll_to(diachi)
        diachi.send_keys("Hoài Đức, Hà Nội")

        # Đăng ký (JS click né quảng cáo)
        btn = self.driver.find_element(
            By.ID, "ContentPlaceHolder1_btDangky"
        )
        self.scroll_to(btn)
        self.js_click(btn)

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class TestTC04:

    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)

    def teardown_method(self):
        self.driver.quit()

    def hide_somee_ads(self):
        # Ẩn banner quảng cáo gây lỗi click
        self.driver.execute_script("""
            var ads = document.querySelectorAll('a[href*="somee.com"]');
            ads.forEach(e => e.style.display='none');
        """)

    def test_TC04_register_success(self):
        driver = self.driver
        wait = self.wait

        # 1. Open website
        driver.get("http://hauiproj.somee.com/Default.aspx")
        driver.set_window_size(894, 767)

        # Ẩn quảng cáo
        self.hide_somee_ads()

        # 2. Click Đăng ký
        wait.until(EC.element_to_be_clickable((By.ID, "LinkDK"))).click()

        # 3. Nhập thông tin đăng ký (KHÔNG click trước)
        wait.until(EC.presence_of_element_located(
            (By.ID, "ContentPlaceHolder1_txtTaiKhoan"))
        ).send_keys("thuan123")

        driver.find_element(
            By.ID, "ContentPlaceHolder1_txtMatKhau"
        ).send_keys("thuan123")

        driver.find_element(
            By.ID, "ContentPlaceHolder1_txtHoTen"
        ).send_keys("Nguyễn Hưng Thuận")

        driver.find_element(
            By.ID, "ContentPlaceHolder1_txtNamSinh"
        ).send_keys("2005-09-04")

        # 4. Chọn giới tính
        gioi_tinh = Select(driver.find_element(
            By.ID, "ContentPlaceHolder1_dllGioiTinh"
        ))
        gioi_tinh.select_by_index(0)

        # 5. Email
        driver.find_element(
            By.ID, "ContentPlaceHolder1_txtEmail"
        ).send_keys("thuan205@gmail.com")

        # 6. SĐT
        driver.find_element(
            By.ID, "ContentPlaceHolder1_txtSdt"
        ).send_keys("0963053320")

        # 7. Địa chỉ (KHÔNG CLICK → không bị che)
        driver.find_element(
            By.ID, "ContentPlaceHolder1_txtDiaChi"
        ).send_keys("Bắc Từ Liêm, Hà Nội")

        # 8. Scroll xuống và click Đăng ký
        btn_dk = driver.find_element(
            By.ID, "ContentPlaceHolder1_btDangky"
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", btn_dk)
        time.sleep(1)
        btn_dk.click()

        # 9. Chờ kết quả (có thể là redirect hoặc thông báo)
        time.sleep(3)

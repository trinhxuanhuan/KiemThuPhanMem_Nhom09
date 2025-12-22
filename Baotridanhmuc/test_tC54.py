import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTC54:
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 20)

    def teardown_method(self):
        self.driver.quit()

    def test_tC54(self):
        self.driver.get("http://hauiproj.somee.com/Default.aspx")
        self.driver.set_window_size(1454, 782)

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

        # Vào danh mục
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#HyperLink5 > li")
            )
        ).click()

        # 🔥 CLICK BẰNG JAVASCRIPT (KHÔNG FAIL)
        cell = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(2)")
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", cell
        )
        self.driver.execute_script(
            "arguments[0].click();", cell
        )

        # Sửa ID
        id_box = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "ContentPlaceHolder1_txtID")
            )
        )
        id_box.clear()
        id_box.send_keys("23")

        self.driver.find_element(
            By.ID, "ContentPlaceHolder1_LinkButton1"
        ).click()

        self.wait.until(
            EC.element_to_be_clickable((By.ID, "LinkDX"))
        ).click()

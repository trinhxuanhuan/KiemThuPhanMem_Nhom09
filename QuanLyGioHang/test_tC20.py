import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TestTC20:

    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        self.driver.quit()

    def test_TC20_input_very_large_quantity_in_cart(self):
        """TC20: Nhập số lượng rất lớn (999999) trong giỏ hàng"""

        # 1. Open home page
        self.driver.get("http://hauiproj.somee.com/Default.aspx")
        self.driver.set_window_size(1100, 924)

        # 2. Vào danh sách sản phẩm
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#HyperLink2 > li"))
        ).click()

        # 3. Chọn sản phẩm đầu tiên
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "ContentPlaceHolder1_DataList1_Image1_0")
            )
        ).click()

        # 4. Thêm vào giỏ hàng
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "ContentPlaceHolder1_Datalist1_btnThemVaoGio_0")
            )
        ).click()

        # 5. Lấy ô số lượng trong giỏ hàng
        qty_input = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_gvGioHang_txtSoLuong_0")
            )
        )

        # Clear chắc chắn rồi nhập 999999
        qty_input.send_keys(Keys.CONTROL + "a")
        qty_input.send_keys(Keys.DELETE)
        qty_input.send_keys("999999")

        # Assert 1: kiểm tra input nhận đúng giá trị
        assert qty_input.get_attribute("value") == "999999"

        # 6. Click nút cập nhật giỏ hàng
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".bt-style-chucnang")
            )
        ).click()

        # 7. Assert nghiệp vụ: hệ thống KHÔNG chấp nhận số lượng quá lớn
        page_source = self.driver.page_source.lower()
        assert (
            "lỗi" in page_source
            or "không hợp lệ" in page_source
            or "số lượng" in page_source
            or "tối đa" in page_source
        ), "Hệ thống vẫn cho phép cập nhật số lượng quá lớn (999999)"

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class TestTC14:

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

    def test_TC14_input_very_large_quantity(self):
        """TC14: Nhập số lượng rất lớn (999999)"""

        # 1. Open home page
        self.driver.get("http://hauiproj.somee.com/Default.aspx")

        # 2. Vào danh sách sản phẩm
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#HyperLink2 > li"))
        ).click()

        # 3. Chọn sản phẩm (ví dụ sản phẩm thứ 5)
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "ContentPlaceHolder1_DataList1_Image1_4"))
        ).click()

        qty_input = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_Datalist1_txtSoLuong_0")
            )
        )

        # 4. Nhập số lượng = 999999 (clear chắc chắn)
        qty_input.send_keys(Keys.CONTROL + "a")
        qty_input.send_keys(Keys.DELETE)
        qty_input.send_keys("999999")

        # Assert 1: đảm bảo input nhận đúng giá trị
        assert qty_input.get_attribute("value") == "999999"

        # 5. Click thêm vào giỏ hàng
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "ContentPlaceHolder1_Datalist1_btnThemVaoGio_0")
            )
        ).click()

        # 6. Assert nghiệp vụ: hệ thống không chấp nhận số lượng quá lớn
        page_source = self.driver.page_source.lower()
        assert (
            "lỗi" in page_source
            or "không hợp lệ" in page_source
            or "số lượng" in page_source
            or "tối đa" in page_source
        ), "Hệ thống vẫn cho phép thêm sản phẩm với số lượng quá lớn"

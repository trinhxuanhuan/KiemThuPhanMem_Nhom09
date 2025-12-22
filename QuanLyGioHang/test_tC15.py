import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BaseTest(unittest.TestCase):
    WAIT_SECONDS = 10

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, self.WAIT_SECONDS)

    def tearDown(self):
        self.driver.quit()

    # ===== helpers =====
    def open(self, url):
        self.driver.get(url)

    def click(self, by, value):
        el = self.wait.until(EC.element_to_be_clickable((by, value)))
        el.click()
        return el

    def type_and_clear(self, by, value, text):
        el = self.wait.until(EC.presence_of_element_located((by, value)))
        el.click()
        el.send_keys(Keys.CONTROL + "a")
        el.send_keys(Keys.DELETE)
        el.send_keys(text)
        return el


class Test_TC15(BaseTest):

    def test_TC15_invalid_quantity_before_add_to_cart(self):
        """TC15: Nhập số lượng -1 và 0 trước khi thêm vào giỏ hàng"""

        # 1. Open home page
        self.open("http://hauiproj.somee.com/Default.aspx")
        self.driver.set_window_size(1100, 924)

        # 2. Vào danh sách sản phẩm
        self.click(By.CSS_SELECTOR, "#HyperLink2 > li")

        # 3. Chọn sản phẩm (ví dụ sản phẩm thứ 7)
        self.click(By.ID, "ContentPlaceHolder1_DataList1_Image1_6")

        qty_input_id = "ContentPlaceHolder1_Datalist1_txtSoLuong_0"
        add_btn_id = "ContentPlaceHolder1_Datalist1_btnThemVaoGio_0"

        # ===== Case 1: nhập -1 =====
        qty_input = self.type_and_clear(By.ID, qty_input_id, "-1")

        # Assert 1: đảm bảo input là -1
        self.assertEqual(qty_input.get_attribute("value"), "-1")

        # Click thêm vào giỏ
        self.click(By.ID, add_btn_id)

        # Assert 2: hệ thống không chấp nhận số lượng âm
        page_source = self.driver.page_source.lower()
        self.assertTrue(
            "lỗi" in page_source
            or "không hợp lệ" in page_source
            or "số lượng" in page_source,
            "Hệ thống vẫn cho phép thêm sản phẩm với số lượng -1"
        )

        # ===== Case 2: nhập 0 =====
        qty_input = self.type_and_clear(By.ID, qty_input_id, "0")

        # Assert 3: đảm bảo input là 0
        self.assertEqual(qty_input.get_attribute("value"), "0")

        # Click thêm vào giỏ
        self.click(By.ID, add_btn_id)

        # Assert 4: hệ thống không chấp nhận số lượng 0
        page_source = self.driver.page_source.lower()
        self.assertTrue(
            "lỗi" in page_source
            or "không hợp lệ" in page_source
            or "số lượng" in page_source,
            "Hệ thống vẫn cho phép thêm sản phẩm với số lượng 0"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

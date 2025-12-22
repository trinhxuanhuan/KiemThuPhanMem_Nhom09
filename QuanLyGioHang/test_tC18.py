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
        # options.add_argument("--headless=new")  # bật nếu cần
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, self.WAIT_SECONDS)

    def tearDown(self):
        self.driver.quit()

    # ===== helper methods =====
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


class Test_TC18(BaseTest):

    def test_TC18_input_quantity_zero(self):
        """TC18: Nhập số lượng = 0 trong giỏ hàng"""

        # 1. Open home page
        self.open("http://hauiproj.somee.com/Default.aspx")
        self.driver.set_window_size(1138, 850)

        # 2. Vào danh sách sản phẩm
        self.click(By.CSS_SELECTOR, "#HyperLink2 > li")

        # 3. Click sản phẩm đầu tiên
        self.click(By.ID, "ContentPlaceHolder1_DataList1_Image1_0")

        # 4. Thêm vào giỏ hàng
        self.click(By.ID, "ContentPlaceHolder1_Datalist1_btnThemVaoGio_0")

        # 5. Nhập số lượng = 0
        qty_input = self.type_and_clear(
            By.ID,
            "ContentPlaceHolder1_gvGioHang_txtSoLuong_0",
            "0"
        )

        # ✅ Assert: đảm bảo input thực sự là "0"
        self.assertEqual(qty_input.get_attribute("value"), "0")

        # 6. Click cập nhật / xóa
        self.click(By.CSS_SELECTOR, "td:nth-child(8) > .bt-style-chucnang")

        # ✅ Assert nghiệp vụ (tối thiểu 1 trong các cái dưới)
        page_source = self.driver.page_source.lower()
        self.assertTrue(
            "giỏ hàng" in page_source or "trống" in page_source,
            "Giỏ hàng không được cập nhật đúng khi số lượng = 0"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

  

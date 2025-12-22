from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTC17:
    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        self.driver.quit()

    def test_tC17(self):
        self.driver.get("http://hauiproj.somee.com/Default.aspx")

        # Vào danh sách sản phẩm
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#HyperLink2 > li"))
        ).click()

        # Mở chi tiết sản phẩm
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "ContentPlaceHolder1_DataList1_Image1_0"))
        ).click()

        # ===== PRECONDITION: thêm vào giỏ =====
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "ContentPlaceHolder1_Datalist1_btnThemVaoGio_0"))
        ).click()

        # ===== SỬA SỐ LƯỢNG =====
        qty = self.wait.until(EC.presence_of_element_located(
            (By.ID, "ContentPlaceHolder1_gvGioHang_txtSoLuong_0"))
        )
        qty.clear()
        qty.send_keys("2")

        self.driver.find_element(
            By.CSS_SELECTOR, "td:nth-child(8) > .bt-style-chucnang"
        ).click()

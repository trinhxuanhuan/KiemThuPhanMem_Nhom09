import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestTC18:

    def setup_method(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 15)  # Tăng timeout vì site chậm

    def teardown_method(self):
        self.driver.quit()

    def test_tC18(self):
        # 1. Mở trang chủ
        self.driver.get("http://hauiproj.somee.com/Default.aspx")

        # 2. Vào danh sách sản phẩm
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#HyperLink2 > li"))
        ).click()

        # 3. Chọn 1 sản phẩm
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "ContentPlaceHolder1_DataList1_Image1_0"))
        ).click()

        # 4. Thêm vào giỏ
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "ContentPlaceHolder1_Datalist1_btnThemVaoGio_0")
            )
        ).click()

        # 5. Vào giỏ hàng
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#HyperLink4 > li"))
        ).click()

        # 6. ÉP số lượng = 0 (BYPASS VALIDATION + FIX APPEND '10')
        qty = self.wait.until(
            EC.presence_of_element_located(
                (By.ID, "ContentPlaceHolder1_gvGioHang_txtSoLuong_0")
            )
        )

        # Script mạnh: xóa sạch value bằng removeAttribute + set '', rồi set '0', trigger mọi event
        self.driver.execute_script("""
            let elem = arguments[0];
            
            // Bypass mọi validation cũ của ASP.NET
            elem.removeAttribute('value');
            elem.value = '';
            
            // Trigger event để JS nhận biết đã xóa
            elem.dispatchEvent(new Event('input', {bubbles: true}));
            elem.dispatchEvent(new Event('change', {bubbles: true}));
            elem.dispatchEvent(new Event('keyup', {bubbles: true}));
            
            // Bây giờ mới set 0
            elem.value = '0';
            elem.setAttribute('value', '0');  // Force attribute
            
            // Trigger đầy đủ event như user gõ thật
            ['input', 'change', 'keyup', 'keydown', 'blur', 'focusout'].forEach(ev => {
                elem.dispatchEvent(new Event(ev, {bubbles: true}));
            });
            
            elem.blur();  // Rời khỏi ô để trigger blur validation
        """, qty)

        time.sleep(1.5)  # Chờ JS validation chạy xong

        # 7. Click nút cập nhật (dùng JS click để chắc chắn)
        update_btn = self.wait.until(
            EC.element_to_be_clickable((
                By.CSS_SELECTOR,
                ".item-data td:nth-child(8) .bt-style-chucnang"
            ))
        )
        self.driver.execute_script("arguments[0].click();", update_btn)

        time.sleep(3)  # Chờ server reload giỏ (site somee.com chậm)

        # 8. Assert giỏ trống
        try:
            self.wait.until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, ".item-data"))
            )
        except:
            pass

        rows = self.driver.find_elements(By.CSS_SELECTOR, ".item-data")
        if len(rows) > 0:
            # Debug thêm: xem số lượng hiện tại là bao nhiêu
            current = self.driver.find_element(By.ID, "ContentPlaceHolder1_gvGioHang_txtSoLuong_0").get_attribute("value")
            print(f"Sau cập nhật, số lượng vẫn là: {current}")

        assert len(rows) == 0, f"FAIL: Giỏ vẫn còn {len(rows)} sản phẩm!"
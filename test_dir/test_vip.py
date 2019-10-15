from conftest import user_name, pwd
from page.vip_page import VipPage


class Testvip:
    """测试vip页"""
    def test_vipopen(self, browser, base_url):
        """进入vip页，"""
        page = VipPage(browser)
        page.get(base_url+'vip')
        page.vip_banner.click()
        page.login_input.send_keys(user_name)
        page.pwd_input = pwd
        page.login_btn.click()
        page.window_scroll(900, 900)
        title = page.get_title
        assert title == '会员资格 | 英荔商学院'



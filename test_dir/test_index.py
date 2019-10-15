

from page.index_page import IndexPage


class TestIndex:
    """首页测试"""
    def test_title(self, browser, base_url):
        """检查url是否正确"""
        page = IndexPage(browser)
        page.get(base_url)
        url = page.get_url
        assert url == 'https://www.elitemba.cn/'
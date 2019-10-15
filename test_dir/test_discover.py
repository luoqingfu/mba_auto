from page.discover_page import DiscoverPage


class TestDiscover:
    """测试发现课程"""
    def test_open(self, browser, base_url):
        """测试打开发现课程，判断url"""
        page = DiscoverPage(browser)
        page.get(base_url)
        page.find_course.click()
        url = page.get_url
        assert url == 'https://www.elitemba.cn/vip'


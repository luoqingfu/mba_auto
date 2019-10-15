from poium import Page, PageElement


class DiscoverPage(Page):
    find_course = PageElement(css='body > div.window-wrap > header > div.main-header > nav > div.main > div:nth-child(2) > a', describe='发现课程按钮')

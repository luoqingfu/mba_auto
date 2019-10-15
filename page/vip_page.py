from poium import Page, PageElement


class VipPage(Page):
    vip_banner = PageElement(css='#content > div > div.banner > a > img.banner-content.banner-pc-img', describe='会员页banner图')
    login_input = PageElement(id_='login-email', describe='账号输入框')
    pwd_input = PageElement(id_='login-password', describe='密码输入框')
    login_btn = PageElement(css='#login > button', describe='登录按钮')
    vip = PageElement(css='#card-box-pc > div > header > div > div > div > a', describe='加入课程')

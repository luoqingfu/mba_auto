# pyautoTest Web UI 自动化项目

#### 特点：

* 全局配置浏览器启动/关闭。
* 测试用例运行失败自动截图。
* 测试用例运行失败可以重跑。
* 测试数据参数化。

#### 安装：

```shell
$ pip install -r requirements.txt
```

#### 配置：

在 __conftest.py__ 文件配置

```python
# 配置浏览器驱动类型。
driver_type = "chrome"

# 配置运行的 URL
url = "https://www.baidu.com"

# 失败重跑次数
rerun = "3"

# 运行测试用例的目录或文件
cases_path = "./test_dir/"
```

#### 运行：

```shell
$ python run_tests.py  (回归模式，生成HTML报告)
$ python run_tests.py -m debug  (调试模式)
```

```python
在page/文件夹下是存放定位信息。
默认定位方式为css='xxxxxx'
id_=''
例如：
login_input = PageElement(id_='login-email', describe='账号输入框')
describe 参数并无实际意义，当你页面元素很多时，用它来增加可读性。

page.get(url)
打开指定的地址

page.xxx.click()
点击指定元素

page.xxx.send_keys('xxx')
输入指定内容到输入框

page.xxx.clear()
清除输入框内的内容

page.xxx.get_title
获取网页title

page.xxx.get_url
获取当前网页地址

page.xxx.text
获取该元素的文字信息

browser.maximize_window()
窗口最大化

browser.refresh()
刷新前网页

browser.back()
后退一页

browser.close()
关闭浏览器

page.window_scroll(x,y)
设置浏览器的长度和宽度（暂时不知道作用）

page.display(css)
显示隐藏元素

page.get_attribute(css, attribute)
获取某个标签的值

page.accept_alert()
同意警告框的内容

page.dismiss_alert()
拒绝警告框的内容

page.get_alert_text()
获取警告框的内容

page.move_to_element(css)
移动到鼠标到指定元素

page.click_and_hold(css)
在元素保持鼠标左键为按下的状态

page.release()
释放鼠标左键的按下状态

page.move_by_offset(x, y）
移动鼠标到指定坐标

page.drag_and_drop_by_offset(x,y)
保持鼠标左键按下，拖动到坐标为x,y







```

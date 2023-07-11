import time
from selenium import webdriver

def create_chrome_driver(*, headless=False):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_arguments('--headless')  # 使用无头模式启动 Chrome 浏览器
    options.add_experimental_option(
        'excludeSwitches', ['enable-automation'])  # 关闭自动化测试提示
    options.add_experimental_option(
        'useAutomationExtension', False)  # 禁用自动化扩展程序

    browser = webdriver.Chrome(options=options)

    # 禁用 navigator.webdriver 属性
    browser.execute_cdp_cmd(
        'Page.addScriptToEvaluateOnNewDocument',
        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
    )
    return browser


if __name__ == '__main__':
    browser = create_chrome_driver()
    browser.get("https://baidu.com")

    time.sleep(15)
    browser.quit()

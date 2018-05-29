from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions


def output_object(target_class):
    def to_object_f(func):
        def func_wrapper(self, *args, **kwargs):
            data = func(self, *args, **kwargs)
            response = []
            for item in data:
                response.append(target_class(*item))

            return response
        return func_wrapper
    return to_object_f


def set_chrome(proxy_str=None):
    options = webdriver.ChromeOptions()
    options.binary_location = "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary"
    options.add_argument("--disable-notifications")
    if proxy_str:
        options.add_argument('--proxy-server={}'.format(proxy_str))
    web_driver = webdriver.Chrome(executable_path="../../resources/chromedriver", chrome_options=options)
    return web_driver

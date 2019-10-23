from selenium import webdriver
from selenium.webdriver import ChromeOptions


# 导入的cookies
cookies=[
    {
        "domain": ".facebook.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "act",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "1564310842523%2F6",
        "id": 1
    },
    {
        "domain": ".facebook.com",
        "expirationDate": 1595846750.631693,
        "hostOnly": False,
        "httpOnly": False,
        "name": "c_user",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "100016227091056",
        "id": 2
    },
    {
        "domain": ".facebook.com",
        "expirationDate": 1627382728.944146,
        "hostOnly": False,
        "httpOnly": True,
        "name": "datr",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "unw9XXNKbLzyd6p3mUmujtQJ",
        "id": 3
    },
    {
        "domain": ".facebook.com",
        "expirationDate": 1595846801.065217,
        "hostOnly": False,
        "httpOnly": True,
        "name": "fr",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "14bVBcyZyKhb6KqnB.AWXrXm8MDjKAS_8G2MjuI7CjL-c.BdPXy6.MA.F09.0.0.BdPX0Q.AWXWbIH_",
        "id": 4
    },
    {
        "domain": ".facebook.com",
        "hostOnly": False,
        "httpOnly": False,
        "name": "presence",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": True,
        "storeId": "0",
        "value": "EDvF3EtimeF1564310805EuserFA21B16227091056A2EstateFDutF1564310805158CEchFDp_5f1B16227091056F1CC",
        "id": 5
    },
    {
        "domain": ".facebook.com",
        "expirationDate": 1627382752.631573,
        "hostOnly": False,
        "httpOnly": True,
        "name": "sb",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "unw9XSj3ECI4rSyosR9RcWyn",
        "id": 6
    },
    {
        "domain": ".facebook.com",
        "expirationDate": 1564400754.43031,
        "hostOnly": False,
        "httpOnly": True,
        "name": "spin",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "r.1000992091_b.trunk_t.1564310754_s.1_v.2_",
        "id": 7
    },
    {
        "domain": ".facebook.com",
        "expirationDate": 1564915645,
        "hostOnly": False,
        "httpOnly": False,
        "name": "wd",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "929x741",
        "id": 8
    },
    {
        "domain": ".facebook.com",
        "expirationDate": 1595846750.631769,
        "hostOnly": False,
        "httpOnly": True,
        "name": "xs",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "46%3Axr91PKBrB-ogGg%3A2%3A1564310751%3A-1%3A-1",
        "id": 9
    }
]

# 缓存文件夹的路径
path=r"E:\fb_adv"

def first():
    global cookies
    print("请进入编辑文件设置cookies,以及路径")
    options=ChromeOptions()
    options.add_argument(r"--user-data-dir=%s"%path)
    driver = webdriver.Chrome(chrome_options=options)  # CHROME_PATH,
    print("正在打开网址")
    driver.get("https://www.facebook.com")
    print("准备导入cookies")
    for cook in cookies:
        driver.add_cookie(cook)
    # cookies=driver.get_cookies()
    print("导入完成，开始刷新页面")
    driver.refresh()
    print("刷新成功!")
    # print(cookies)
    a=input("????")

    driver.quit()

if __name__ == '__main__':
    first()
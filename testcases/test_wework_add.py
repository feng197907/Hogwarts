from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeworkAdd:

    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:62001"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
        caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
        # caps['dontStopAppOnReset'] = 'true'    # 启动之前不停止app
        caps['settings[waitForIdleTimeout]'] = 0

        # 与server 建立连接,初始化一个driver 创建session,返回一个sessionid
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    def teardown_class(self):
        self.driver.quit()

    def test_wework_add(self):
        ele1 = self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]')
        ele1.click()

        ele2 = self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成员"]')
        ele2.click()

        ele3 = self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hgx')
        ele3.click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/awt').send_keys('112233')
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/f1e').send_keys('14213456781')
        self.driver.find_element(MobileBy.XPATH, '//*[@text="设置部门"]').click()
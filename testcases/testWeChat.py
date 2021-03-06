from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import time

"""
改造1：pytest
"""


class TestWeChat:

    def setup(self):
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

    """打卡功能
    """

    def test_daka(self):
        # 步骤1：点击工作台
        # el1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[3]/android.widget.TextView")
        el1 = self.driver.find_element(MobileBy.XPATH,
                                       "//*[@text='工作台']")
        el1.click()
        # 滚动查找 "打卡" 元素
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'text("打卡").instance(0));')
        # el2 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[10]/android.widget.LinearLayout/android.widget.TextView")
        # el3 = self.driver.find_element_by_id("com.tencent.wework:id/gcx")
        # time.sleep(2)
        daka_btn = 'resourceId("com.tencent.wework:id/el8").text("打卡")'
        self.driver.find_element_by_android_uiautomator(daka_btn).click()

        # 点击"外出打卡"
        # el3 = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gcx")
        el3 = self.driver.find_element_by_android_uiautomator('resourceId("com.tencent.wework:id/gw8").text("外出打卡")')
        el3.click()

        # 点击 第N次外出打卡
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text, '次外出')]").click()

        # 验证打卡成功
        # result = self.driver.find_element(MobileBy.ID,
        #                                   'com.tencent.wework:id/mk').text
        result = self.driver.find_element_by_android_uiautomator('resourceId("com.tencent.wework:id/n7").text("外出打卡成功")').text

        assert '打卡成功' in result

    def teardown(self):
        # 消毁session
        self.driver.quit()

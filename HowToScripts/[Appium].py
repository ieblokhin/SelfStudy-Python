from appium import webdriver
# from appium.webdriver.appium_connection import RemoteConnection

desired_caps = {
    "platformName": "Android",
    "platformVersion": "11",
     "deviceName": "Pixel4",
     "automationName": "UiAutomator2",
     "appPackage": "com.google.android.apps.youtube.music",
     "appActivity": "com.google.android.apps.youtube.music.activities.MusicActivity"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# from lib2to3.pgen2 import driver
# import profile
# from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# from selenium import webdriver

# profile_path = r'C:\Users\AZIZ PC\AppData\Roaming\Mozilla\Firefox\Profiles\3r52zcrf.default'
# options = Options()
# options.set_preference('profile', profile_path)
# service = Service(r'G:\Apps\geckodriver.exe')
# driver = Firefox(service=service, options=options)
from csv import DictReader
from cv2 import repeat
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import schedule
PATH = Service("C:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

def absen():
    driver.get("http://elearning.bsi.ac.id/login")
    email = driver.find_element_by_name("username")
    email.send_keys("17200693")
    pw = driver.find_element_by_name("password")
    pw.send_keys("@1ahKuwa09")
    button = driver.find_element_by_tag_name("Button")
    button.click()
    jadwal = driver.find_element_by_id("pin-sidebar")
    jadwal = driver.find_element_by_class_name("sidebar-dropdown")
    jadwal.click()
    jadwal0 = driver.find_element_by_xpath(
        "/html/body/div[1]/nav/div/div[1]/div/ul/li[4]/a/span")
    jadwal0.click()
    pel = driver.find_element_by_xpath(
        "/html/body/div[1]/nav/div/div[1]/div/ul/li[4]/div/ul/li[1]/a"
    ).click()
    try:
        masuk = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/a[1]").click()
        absen = driver.find_element_by_xpath(
            "//button[@type='submit']").click()
        komentar = driver.find_element_by_name("komentar")
        komentar.send_keys("Selalu semangat")
        kirimkomen = driver.find_element_by_class_name("icon-send1").click()
        driver.quit()
    except:
        driver.quit()


absen()

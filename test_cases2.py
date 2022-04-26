import time
import unittest
from selenium import webdriver
from pageObjects.Report_Worklist import Worklist

class test_cases2(unittest.TestCase):
    exec_path = "C:\\Users\\User\\Documents\\chromedriver.exe"
    base_URL = "https://fibersafe.tmrnd.com.my:86/portal/login"
    username = "PLTest0134"
    password = "Test1234"

    @classmethod
# pass in a service object driver & initialize webdriver
# open url and maximize window
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=cls.exec_path)
        cls.driver.get(cls.base_URL)
        cls.driver.maximize_window()
        time.sleep(3)

#call each function from the LoginPage class
    def test_cases2(self):
        self.lp = Worklist(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        time.sleep(10)
        self.lp.reports()
        time.sleep(5)
        self.lp.worklist()
        time.sleep(20)
        # self.lp.searchstatusupcoming()
        # time.sleep(10)
        # self.lp.searchstatusinprogress()
        # time.sleep(10)
        # self.lp.selectfieldteammember1()
        # time.sleep(5)
        # self.lp.test_calendar_control_range1()
        # time.sleep(5)
        # self.lp.updatestatus()
        # time.sleep(5)
        # self.lp.fibercut()
        # time.sleep(10)
        # self.lp.searchstatussubmitted()
        # time.sleep(5)
        # self.lp.test_calendar_control_range2()
        # time.sleep(10)
        self.lp.searchstatusdecline()
        time.sleep(5)
        self.lp.selectfieldteammember3()
        time.sleep(5)
        self.lp.test_calendar_control_range3()
        time.sleep(10)
        self.lp.searchstatusinvalid()
        time.sleep(5)
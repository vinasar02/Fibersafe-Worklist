import time
import pytest
from selenium import webdriver
from pageObjects.Report_Worklist import Worklist

class TestCases2():
    exec_path = "C:\\Users\\User\\Documents\\chromedriver.exe"
    base_URL = "https://fibersafe.tmrnd.com.my:86/portal/login"
    username = "PLTest0134"
    password = "Test1234"


    @pytest.fixture()
# pass in a service object driver & initialize webdriver
# open url and maximize window
    def Test_setup(self):
        self.driver = webdriver.Chrome(executable_path=self.exec_path)
        self.driver.get(self.base_URL)
        self.driver.maximize_window()
        time.sleep(3)
        yield
        self.driver.close()
        self.driver.quit()


#call each function from the LoginPage class
    def test_cases2(self,Test_setup):
        self.lp = Worklist(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        time.sleep(10)
        self.lp.reports()
        time.sleep(5)
        self.lp.worklist()
        time.sleep(20)
        self.lp.searchstatusupcoming()
        time.sleep(10)
        self.lp.searchstatusinprogress()
        time.sleep(10)
        self.lp.selectfieldteammember1()
        time.sleep(5)
        self.lp.test_calendar_control_range1()
        time.sleep(5)
        self.lp.updatestatus()
        time.sleep(5)
        self.lp.fibercut()
        time.sleep(10)
        self.lp.searchstatussubmitted()
        time.sleep(5)
        self.lp.test_calendar_control_range2()
        time.sleep(10)
        self.lp.searchstatusdecline()
        time.sleep(10)
        self.lp.selectfieldteammember3()
        time.sleep(5)
        self.lp.test_calendar_control_range3()
        time.sleep(10)
        self.lp.searchstatusinvalid()
        time.sleep(5)


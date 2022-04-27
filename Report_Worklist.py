import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class Worklist:
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_xpath = "/html/body/div/div/div[2]/div/div/div/div/div[2]/form/div[3]/button"

    def __init__(self, driver):
        self.driver = driver

############################## LOGIN ############################################################

# set the username
    def setusername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
# set the password
    def setpassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
# click the login button
    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

################################ REPORT #############################################
# expand the bar
    def reports(self):
        expand = self.driver.find_element(By.XPATH,"/html/body/div[1]/nav/div/div/ul[1]/div[1]/li/a")
        expand.click()
# view the worklist
    def worklist(self):
        clickoption = self.driver.find_element(By.XPATH, "/html/body/div[1]/nav/div/div/ul[1]/div[1]/li/div/ul/li[3]/a")
        clickoption.click()
        time.sleep(15)

# ///////////////////////////////////////////////////// STATUS : UPCOMING //////////////////////////////////////////////////////////////////////#
# enter the status "UPCOMING" at the search box
    def searchstatusupcoming(self):
        search1 = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/label/input')
        search1.send_keys('Upcoming')
        time.sleep(5)
# click the search button
        clicksearch = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/i")
        clicksearch.click()
        time.sleep(5)
# choose any of the user from the list
        i = random.randint(1, 10)
        choice2 = self.driver.find_element(By.XPATH, '//*[@id="user-table"]/tbody/tr[' + str(i) + ']')
        print(choice2)
        choice2.click()
        time.sleep(5)
# back to the list of the worklist
        backbutton = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/button/div/span")
        backbutton.click()
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/label/input').clear()
        time.sleep(10)

# ///////////////////////////////////////////////////// STATUS : IN PROGRESS //////////////////////////////////////////////////////////////////////#
# enter the status "IN PROGRESS" at the search box
    def searchstatusinprogress(self):
        search1 = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/label/input')
        search1.send_keys('In progress')
        time.sleep(5)
# click the search button
        clicksearch = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/i")
        clicksearch.click()
        time.sleep(5)
# choose any of the user from the list
        i = random.randint(1, 10)
        choice2 = self.driver.find_element(By.XPATH, '//*[@id="user-table"]/tbody/tr[' + str(i) + ']')
        print(choice2)
        choice2.click()
        time.sleep(5)
# edit the field team member
    def selectfieldteammember1(self):
        edit = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[3]/i")
        edit.click()
        time.sleep(5)
#select any of the field team member name
        select1 = Select(self.driver.find_element_by_id("assignee_upd"))
        select1.select_by_visible_text("Wut Hmone Hnin Hlaing")
        time.sleep(5)
# enter the remark for the field team member
        remark = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/textarea')
        remark.send_keys('Test')
        time.sleep(5)
# click "x" button
        clickcancel= self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div/div[2]/div[1]/div/i")
        clickcancel.click()
# set the date of visit
    def test_calendar_control_range1(self):
        frame = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div")
        frame.click()
        time.sleep(5)
        year = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div/div[2]/div[2]/div/table/thead/tr[1]/th[2]")
        year.click()
        time.sleep(5)
        month = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div/div[2]/div[2]/div/table[2]/tbody/tr[2]/td[1]")
        month.click()
        time.sleep(5)
        day = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[1]")
        day.click()
        time.sleep(5)
# save the changes
        save = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[3]/i[2]")
        save.click()
        time.sleep(5)
# back to the list of the worklist
        backbutton = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/button/div/span")
        backbutton.click()
        time.sleep(20)
# update the status of inspection
    def updatestatus(self):
# choose any of the user from the list
        i = random.randint(1,10)
        choice2 = self.driver.find_element(By.XPATH, '//*[@id="user-table"]/tbody/tr['+str(i)+']')
        print(choice2)
        choice2.click()
        time.sleep(5)
# click the see details button
        seedetails = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[1]/div/div/span[3]/button")
        seedetails.click()
        time.sleep(5)
# change the inspection status by clicking the edit button
        inspection_status = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[1]/i")
        inspection_status .click()
        time.sleep(5)
        select1 = Select(self.driver.find_element_by_id("status_upd"))
        select1.select_by_visible_text("Completed")
        time.sleep(5)
# enter the remark for the status updated
        remark = self.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/textarea')
        remark.send_keys('Complete')
        time.sleep(5)
#is there any fibercut
    def fibercut(self):
# is therere any fibercut by clicking the edit button
        editclick = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[3]/i")
        editclick .click()
        time.sleep(5)
#click the box if yes
        click_box = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[2]/div[2]/label/input")
        click_box.click()
        time.sleep(5)
# enter the remark for the status updated
        remark = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[3]/div[2]/textarea")
        remark.send_keys('Cable')
        time.sleep(5)
# click the submit button
        submit = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div/div/div[2]/div/div[5]/button/span[2]")
        submit.click()
        time.sleep(5)
# back to the inspection
        backbutton = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/button/div/span")
        backbutton.click()
        time.sleep(3)
# back to the list of the worklist
        backbutton = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/button/div/span")
        backbutton.click()
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/label/input').clear()
        time.sleep(10)


#///////////////////////////////////////////////////// STATUS : SUBMITTED //////////////////////////////////////////////////////////////////////#
# enter the status "SUBMITTED" at the search box
    def searchstatussubmitted(self):
        search1 = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/label/input')
        search1.send_keys('Submitted')
        time.sleep(5)
# click the search button
        clicksearch = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/i")
        clicksearch.click()
        time.sleep(5)
# choose any of the user from the list
        i = random.randint(1, 10)
        choice2 = self.driver.find_element(By.XPATH, '//*[@id="user-table"]/tbody/tr[' + str(i) + ']')
        print(choice2)
        choice2.click()
        time.sleep(5)
# click the see details button
        seedetails = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[1]/div/div/span[3]/button")
        seedetails.click()

# scroll down to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

# edit the revisit
        editrevisit = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/i")
        editrevisit.click()
        time.sleep(5)

# click the require revisit
        require = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[2]/label/input")
        require.click()
        time.sleep(5)

# click "x" button
#         clickcancel = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div[1]/div/i")
#         clickcancel.click()

#set the date of visit
    def test_calendar_control_range2(self):
        frame = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[4]/div[1]")
        frame.click()
        time.sleep(5)
        year = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[4]/div[1]/div[2]/div[2]/div/table/thead/tr[1]/th[2]")
        year.click()
        time.sleep(5)
        month = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[4]/div[1]/div[2]/div[2]/div/table[2]/tbody/tr[2]/td[1]")
        month.click()
        time.sleep(5)
        day = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[3]/div[4]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[1]")
        day.click()
        time.sleep(5)
#click the submit button
        submit = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[3]/div[2]/div/div/div[2]/div/div[4]/button/span[2]")
        submit.click()
        time.sleep(5)
# back to the inspection
        backbutton = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/button/div/span")
        backbutton.click()
        time.sleep(5)
# back to the list of the worklist
        backbutton = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/button/div/span")
        backbutton.click()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/label/input").clear()
        time.sleep(10)

# ///////////////////////////////////////////////////// STATUS : DECLINE//////////////////////////////////////////////////////////////////////#
# enter the status "DECLINE" at the search box
    def searchstatusdecline(self):
        search1 = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/label/input')
        search1.send_keys('Decline')
        time.sleep(5)
# click the search button
        clicksearch = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/i")
        clicksearch.click()
        time.sleep(5)
# choose any of the user from the list
        i = random.randint(1, 10)
        choice2 = self.driver.find_element(By.XPATH, '//*[@id="user-table"]/tbody/tr[' + str(i) + ']')
        print(choice2)
        choice2.click()


# edit the field team member
    def selectfieldteammember3(self):
        edit = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[3]/i")
        edit.click()
        time.sleep(5)
# select any of the field team member name
        select1 = Select(self.driver.find_element_by_id("assignee_upd"))
        select1.select_by_visible_text("arfan FT 2")
        time.sleep(5)
# enter the remark for the field team member
        remark = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/textarea')
        remark.send_keys('Test')
        time.sleep(5)

#set the date of visit
    def test_calendar_control_range3(self):
        frame = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div")
        frame.click()
        time.sleep(5)
        year = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div/div[2]/div[2]/div/table/thead/tr[1]/th[2]")
        year.click()
        time.sleep(5)
        month = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div/div[2]/div[2]/div/table[2]/tbody/tr[2]/td[1]")
        month.click()
        time.sleep(5)
        day = self.driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[5]/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[1]")
        day.click()
        time.sleep(5)
# save the changes
        save = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/div[3]/i[2]")
        save.click()
        time.sleep(5)
# back to the list of the worklist
        backbutton = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/button/div/span")
        backbutton.click()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/label/input").clear()
        time.sleep(10)

# ///////////////////////////////////////////////////// STATUS : INVALID //////////////////////////////////////////////////////////////////////#
# enter the status "INVALID" at the search box
    def searchstatusinvalid(self):
        search1 = self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/label/input')
        search1.send_keys('Invalid')
        time.sleep(5)
# click the search button
        clicksearch = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/i")
        clicksearch.click()
        time.sleep(5)
# choose any of the user from the list
        i = random.randint(1, 10)
        choice2 = self.driver.find_element(By.XPATH, '//*[@id="user-table"]/tbody/tr[' + str(i) + ']')
        print(choice2)
        choice2.click()
        time.sleep(5)
# back to the list of the worklist
        backbutton = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/div[1]/div/div[2]/button/div/span")
        backbutton.click()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/label/input").clear()
        time.sleep(10)
# click the download button to download the worklist document
        download = self.driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div/button[1]/div/i")
        download.click()
        time.sleep(25)
# Go to main dashboard
        back = self.driver.find_element(By.XPATH, "/html/body/div/nav/div/div/ul[1]/li[1]/a")
        back.click()

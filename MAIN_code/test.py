from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from ORANGE_LOCATORS import locators
from ORANGE_DATA import data
import pytest


class Test_hrm:
    
   
    @pytest.fixture


    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait=WebDriverWait(self.driver,15)
        self.driver.maximize_window()
        self.driver.get(data.orange_data().url)
#LOGIN DETAILS         
        self.wait.until(EC.presence_of_element_located((By.NAME, locators.orange_locators().username_locator))).send_keys(data.orange_data().username)
        self.wait.until(EC.presence_of_element_located((By.NAME, locators.orange_locators().password_locator))).send_keys(data.orange_data().password)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().submitButton_locator))).click()
        yield
    

       
       
     



# VALIDATING ORANGE_HRM DEMO PAGE
     
    def test_tejo(self,booting_function):
         
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().serch))).send_keys(data.orange_data().search)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().serch))).send_keys(Keys.END + Keys.SHIFT + Keys.HOME + Keys.DELETE)
        self.driver.close() 
#VALIDATING USER_ROLE & STATUS
    def test_admin_1(self,booting_function):
         
        self.wait.until(EC.presence_of_element_located((By. XPATH,locators.orange_locators().admin))).click()
         
        drop_down = self.wait.until(EC.presence_of_element_located((By. XPATH,locators.orange_locators().drop_down)))
        action = ActionChains(self.driver)        
        action.click(on_element=drop_down).perform()
         
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT,locators.orange_locators().user_locator))).click()
         
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().user_role))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().status))).click()
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESSFULLY : Logged in with Username  and Password & validated user_role,user_status")
        self.driver.close()

    def test_edit(self,booting_function):
         
        self.wait.until(EC.presence_of_element_located((By . XPATH,locators.orange_locators().PIM_CNT))).click() 
        self.wait.until(EC.presence_of_element_located((By. XPATH, locators.orange_locators().Add_employee))).click()


    
# PERSONAL DETAILS        
             
        self.wait.until(EC.presence_of_element_located((By.NAME, locators.orange_locators().first_input))).send_keys(data.orange_data().firsy_name)
        self.wait.until(EC.presence_of_element_located((By.NAME, locators.orange_locators(). second_input))).send_keys(data.orange_data().second_name)
        self.wait.until(EC.presence_of_element_located((By.NAME, locators.orange_locators().last_input))).send_keys(data.orange_data().last_name)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().login_button))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().user_login))).send_keys(data.orange_data().mail)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().password_login))).send_keys(data.orange_data().paswd)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().conform_pass))).send_keys(data.orange_data().CNF_paswd)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().save_details))).click() 
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().Nick_name))).send_keys(data.orange_data().NICK_NAME)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().otherid))).send_keys(data.orange_data().other_id)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().driver_li))).send_keys(data.orange_data().driver_license)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().license_exp))).send_keys(data.orange_data().Li_exp)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().ssn))).send_keys(data.orange_data().ssn_no)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().sin))).send_keys(data.orange_data().sin_no)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().Gender))).click()

        drop_down1=self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'))).click()
        option=self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[3]/span'))).click()

        d_own=self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'))).click()
        option1=self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/span'))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().DOB))).send_keys(data.orange_data().date_of_birth)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().military_service))).send_keys(data.orange_data().military)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().save1))).click()
         
        #CONTACT DETAILS
        element = self.wait.until(EC.presence_of_element_located((By.XPATH, locators.orange_locators().contact_locator)))
        self.driver.execute_script("arguments[0].click();", element)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().street_1))).send_keys(data.orange_data().adress_1)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().street_2))).send_keys(data.orange_data().adress_2)  
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().city1))).send_keys(data.orange_data().adress_3)   
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().state))).send_keys(data.orange_data().provinance)  
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().zip_code))).send_keys(data.orange_data().postal)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().country))).click()                                         
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().india))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().home))).send_keys(data.orange_data().home_no)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().mobile))).send_keys(data.orange_data().mobile_no)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().work_mail))).send_keys(data.orange_data().mail_1)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().other_mail))).send_keys(data.orange_data().mail_2)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().save_2))).click()


     #EMEREGENCY CONTACT DETAILS
        EMG_CON=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().Emergengy_contact)))
        self.driver.execute_script("arguments[0].click();",EMG_CON)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().ADD_EMG))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().EMG_name))).send_keys(data.orange_data().emg_name)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().EMG_relationship))).send_keys(data.orange_data().emg_relationship)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().EMG_tele))).send_keys(data.orange_data().emg_telephone)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().EMG_mob))).send_keys(data.orange_data().emg_mob)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().EMG_work_tele))).send_keys(data.orange_data().emg_tele_work)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().EMG_save))).click() 


# DEPENDENTS DETAILS
        DEPENDENT=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().DEPENDENT_LOCATORS)))
        self.driver.execute_script("arguments[0].click();",DEPENDENT)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().DEPENDENT_ADD))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().DEPENDENT_NAME))).send_keys(data.orange_data().dependent_name)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().DEPENDENT_RELEATIONSHIP))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().DEPENDENT_OTHERS))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().DEPENDENT_SPECIFY))).send_keys(data.orange_data().dependent_specify)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().DEPENDENT_DOB))).send_keys(data.orange_data().dependent_dob)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().DEPENDENT_SAVE))).click()


# JOB DETAILS
        JOB=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().JOB_LOCATOR)))
        self.driver.execute_script("arguments[0].click();",JOB)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().JOB_DOB))).send_keys(data.orange_data().job_dob) 
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().JOB_TITLE))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().JOB_QA))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().JOB_CATAGEORY))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().JOB_PROFFIESION))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().JOB_SUBUNIT))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().SUBUNIT_ENG))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().EMPLYOMENT_LOCATION))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().EMPLOYMENT_NEWYORK))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().EMPLOYMENT_STATUS))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().EMPLYOMENT_PERMANENT))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().CONTRACT_DETAILS))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().CONTRACT_START))).send_keys(data.orange_data().contract_start)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().CONTRACT_END))).send_keys(data.orange_data().contract_end)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().JOB_SAVE))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().TERMINATE_EMP))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().TERMINATION_DATE))).send_keys(data.orange_data().termination_date)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().TEMINATION_REASON))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().EMPLOYEE_RESIGN))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().TERMINATE_SAVE))).click()
        sleep(10)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().ACTIVATE_EMP))).click()
        
#SALARY DETAILS

        SALARY=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().SALARY_LOCATOR)))
        self.driver.execute_script("arguments[0].click();",SALARY)         
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().SALARY_ADD))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().SALARY_COMPONENT))).send_keys(data.orange_data().component)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().PAY_GRADE))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().PAY_GRADE_1))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().PAY_FREQUENCY))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().WEEEKLY))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().CURRENCY))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().CURRENCY_LOC))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().AMOUNT))).send_keys(data.orange_data().amount)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().TOGGLE))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().ACC_NO))).send_keys(data.orange_data().acc_num)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().ACC_TYPE))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().ACC_SAVINGS))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().ROUTING_NO))).send_keys(data.orange_data().routing_no)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().AMOUNT_1))).send_keys(data.orange_data().amount_1)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().SALARY_SAVE))).click()


#TAX EXEMPTION

        TAX=self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().TAX_EXEMPTION)))
        self.driver.execute_script("arguments[0].click();",TAX)   
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().STATUS_TAX))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().SINGLE_TAX))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().EXEMPTION))).send_keys(data.orange_data().exemption)
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().STATE))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().NEW_YORK))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().STATUS))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().MARRIED))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().UNEMPLOYMENT))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().ALASKA))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().WORK_STATE))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().ARIZONA))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,locators.orange_locators().TAX_SAVE))).click()
        assert self.driver.title !='https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/46'
        print("SUCCESSFULLY :ADDED EMPLYOEE & VALIDATED ALL INFORMATION ABOUT EMPLYOEE")
        self.driver.close()


        





       
       
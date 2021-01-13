from selenium import webdriver
import time
import names
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from random import randint
from selenium.webdriver.support.wait import WebDriverWait


class T:

   def randomGenerator(self):

      global First_name
      First_name = names.get_first_name()


   def openBrowser(self):
      options = Options()
      options.add_argument('--allow-running-insecure-content')
      options.add_argument('--ignore-certificate-errors')
      print(">>Open Browser: START")
      self.CovidIdentifier = webdriver.Chrome(r"C:\Users\laxma\Downloads\chromedriver\chromedriver.exe",options=options)
      self.CovidIdentifier.set_window_position(-2000, 0)
      self.CovidIdentifier.maximize_window()
      self.CovidIdentifier.get("http://127.0.0.1:8000/")
      time.sleep(3)
      print("Open Browser: END<<")

   def closeBrowser(self):
      print(">>Close Browser: START")
      self.CovidIdentifier.close()
      print("Close Browser: END<<")

   def login(self, userid, pwd):
      print(">>LogIn: START")
      self.CovidIdentifier.find_element_by_css_selector("div.col-md-12>nav>ul>li:nth-child(3)>a").click()
      self.CovidIdentifier.find_element_by_id("id_username").send_keys(userid)
      self.CovidIdentifier.find_element_by_id("id_password").send_keys(pwd)
      self.CovidIdentifier.find_element_by_css_selector("input.alert.alert-success").submit()
      time.sleep(3)
      print("LogIn: END<<")


   def logout(self):
      print(">>LogOut: START")
      time.sleep(3)
      self.CovidIdentifier.find_element_by_css_selector(" div.header>div>ul>li>a").click()
      time.sleep(2)
      print("LogOut: END<<")

   def PasswordChange(self,oldpassword,newpassword):
      self.CovidIdentifier.find_element_by_css_selector(" #settings>a").click()
      time.sleep(2)
      self.CovidIdentifier.find_element_by_css_selector("#settings>div>a:nth-child(1)").click()
      time.sleep(2)
      self.CovidIdentifier.find_element_by_css_selector("#id_old_password").send_keys(oldpassword)
      self.CovidIdentifier.find_element_by_css_selector("#id_new_password1").send_keys(newpassword)
      self.CovidIdentifier.find_element_by_css_selector("#id_new_password2").send_keys(newpassword)
      time.sleep(2)
      self.CovidIdentifier.find_element_by_css_selector(" form > input.alert.alert-success").click()

   def Questionaries(self):
      time.sleep(2)
      self.CovidIdentifier.find_element_by_css_selector("p:nth-child(2)>input[type=radio]").click()
      time.sleep(2)
      self.CovidIdentifier.find_element_by_css_selector("#test>div:nth-child(3)>p:nth-child(2)>input[type=radio]").click()

      findme = self.CovidIdentifier.find_element_by_css_selector("#test > input[type=button]:nth-child(17)")
      time.sleep(1)

      ## Scroll down the page till the selected element is visual

      self.CovidIdentifier.execute_script("arguments[0].scrollIntoView();", findme)
      time.sleep(1)
      self.CovidIdentifier.find_element_by_css_selector("#test>input[type=button]:nth-child(17)").click()
      myresultvalue = int(self.CovidIdentifier.find_element_by_css_selector("#demo").text)

      if myresultvalue:
         try:
            assert int(4) == int(myresultvalue)
         except:
            print("There is additional bug || Additional bug")

         finally:
            print("resultValue: ", myresultvalue)
            print("Verification of result  Details: END||<<")

   def Visualization_check(self):
      time.sleep(1)
      self.CovidIdentifier.find_element_by_css_selector("#messages>a>span").click()
      time.sleep(1)
      self.CovidIdentifier.find_element_by_css_selector("#messages>div>a>span").click()
      time.sleep(1)
      self.CovidIdentifier.find_element_by_css_selector("div.col-lg-4>input:nth-child(3)").click()

   def ProfileCheck(self):
      time.sleep(2)
      self.CovidIdentifier.find_element_by_css_selector("#profile>a").click()
      time.sleep(2)
      self.CovidIdentifier.find_element_by_css_selector("#profile>div:nth-child(2)>a>span").click()
















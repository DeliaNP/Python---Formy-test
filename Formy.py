import time

import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from assertpy import soft_assertions, assert_that  #?????

class Formy(unittest.TestCase):
    LINK="https://formy-project.herokuapp.com/form"
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://formy-project.herokuapp.com/form")
        self.driver.maximize_window()
        time.sleep(3)

#TODO: fill in first name
    def test_first_name(self):
        first_name=self.driver.find_element(By.ID, "first-name")
        first_name.send_keys("delia")
        time.sleep(2)

#TODO: fill in last name
    def test_last_name(self):
        last_name=self.driver.find_element(By.ID, "last-name")
        last_name.send_keys("parvu")
        time.sleep(2)

# TODO: complete job title
    def test_job_title(self):
        job_title=self.driver.find_element(By.XPATH, '//input[@placeholder="Enter your job title"]')
        job_title.send_keys('evaluator')
        time.sleep(2)

#TODO: complete educational level
    def test_grad_school(self):
        # grad_school=self.driver.find_element(By.CLASS_NAME,"col-sm-8.col-sm-offset-2")  # nu a dat eroare, dar nu am vazut bifa
        grad_school=self.driver.find_element(By.XPATH, '//input[@id="radio-button-3"]')
        grad_school.click()
        time.sleep(2)

#TODO: complete "gender"
    def test_gen(self):
        gen=self.driver.find_element(By.XPATH, '//input[@id="checkbox-2"]')
        gen.click()
        time.sleep(2)

#TODO: select experience
    def test_experience(self):
        experience=self.driver.find_element(By.XPATH, '//select[@id="select-menu"]')  #vreau sa vad care sunt optiunile
        experience.click()
        time.sleep(2)
        experience1=self.driver.find_element(By.XPATH, '//option[@value="3"]')
        experience1.click()
        time.sleep(2)

#TODO: camplete data
    def test_date(self):
        date=self.driver.find_element(By.XPATH, '//input[@data-date-today-highlight="true"]')
        date.click()
        #date.send_keys("04/15/2024")  # scriu manual data
        date1=self.driver.find_element(By.XPATH, '//td[@class="today day"]')
        date1.click()
        time.sleep(4)

#TODO: the submit button, is active/visible
    def test_submit(self):
        submit=self.driver.find_element(By.XPATH, '//a[@role="button"]')
        #assert submit.is_displayed()
        submit.click()
        time.sleep(2)

#TODO: check if the form has been completed
    def test_formular(self):
        submit = self.driver.find_element(By.XPATH, '//a[@role="button"]')
        submit.click()
        time.sleep(3)
        message_succes=self.driver.find_element(By.XPATH, "//h1[@align='center']")
        if message_succes.is_displayed():
            print('Formular completat corect')
        else:
            print("Rulare eronata")
        self.assertEqual(message_succes.text,"Thanks for submitting your form")
        # textul din formular este egal cu textul mentionat aici(string)
        with soft_assertions():
            assert_that(message_succes.text).contains("submitting")  # daca formularul contine cuvantul dat



    def tearDown(self):
        self.driver.quit()



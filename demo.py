#Simple assignment
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tkinter import *
from selenium import *
from selenium.webdriver.common.action_chains import ActionChains


class Tinderbot:
    def __init__(self,email,passw):
        cp = webdriver.ChromeOptions()
        cp.add_argument("--disable-notifications")
        driver = Chrome(options=cp)
        driver.implicitly_wait(3)
        self.driver = driver
        actions = ActionChains(driver)
        driver.get("https://tinder.com/")
        time.sleep(2)
        facebook = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        facebook.click()
        driver.switch_to.window(driver.window_handles[1])
        self.email = email
        self.passw = passw
        idtext = driver.find_element_by_id("email")
        idtext.send_keys(email)
        password = driver.find_element_by_id("pass")
        password.send_keys(passw, Keys.ENTER)
        driver.switch_to.window(driver.window_handles[0])
        # time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()

    def infinitelike(self,delay):  # method that autolikes the next person after a delay
        try:
            for i in range (0,100):
                likebutton = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
                likebutton.click()
                time.sleep(delay)
        except:
            try:
                self.ridofpopup1()
            except:
                self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a').click()
            self.infinitelike(delay)
    def infinitedislike(self,delay):  #loop dislike (test method)
            try:
                for i in range (0,20):
                    dislikebutton = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
                    dislikebutton.click()
                    time.sleep(delay)
            except:
                if EXCEPTION == 8:  
                    self.ridofpopup1()
                self.infinitedislike(delay)
    def ridofpopup1(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]').click()
        except:
            pass


e = "alexboyuchen@gmail.com"
p = "2000118tten"

T=Tinderbot(e,p)
T.infinitedislike(1)





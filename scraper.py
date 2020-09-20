# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:54:07 2020

@author: saikrishnavuta
"""

#Using selenium for scrapping
from selenium import webdriver

#If you are using chrome browser for scrapping download the below executable file and navigate to it
#Not included in the project. Download and change the path to work smoothly.
chrome_path= r"C:\Users\saikrishnavuta\Desktop\My_projects\ml\Data scraping\chromedriver_win32\chromedriver.exe"

#To open the chrome browser
driver= webdriver.Chrome(chrome_path)

#Allows you to maximize the browser
driver.maximize_window()

#This navigates to the required page you want to scrap data
driver.get("https://www.iplt20.com/stats/2019/most-runs")

#To perform a scroll operation on the page
driver.execute_script("window.scrollTo(0,100)")

#Scraping data from the score table
row_count=len(driver.find_elements_by_xpath("""//*[@id="main-content"]/div[2]/div/div/div[3]/table/tbody/tr"""))
col_count=len(driver.find_elements_by_xpath("""//*[@id="main-content"]/div[2]/div/div/div[3]/table/tbody/tr[1]/th"""))

#Created a file to store the data scraped
fl=open("batsman.csv", mode="w+")

for i in range(1,row_count+1):
    data=""
    for j in range(1, col_count+1):
        xpath="""//*[@id="main-content"]/div[2]/div/div/div[3]/table/tbody/tr["""+str(i)
        if(i==1):
            xpath+="]/th["+str(j)+"]"
        else:
            xpath+="]/td["+str(j)+"]"
        
        data+=driver.find_element_by_xpath(xpath).text+","
    if(i==1):
        fl.write(data+"Team,Role,Style,Nationality,\n")
    else:
        secondpg="""//*[@id="main-content"]/div[2]/div/div/div[3]/table/tbody/tr["""
        secondpg+=str(i)+"]/td[2]/div[2]/div[2]/a/span"
        playerdata=driver.find_element_by_xpath(secondpg).click()
        teamName=driver.find_element_by_xpath("""/html/body/div[4]/div[1]/div/div/h1""").text
        try:
            playerDetails=driver.find_elements_by_class_name('player-details__value')
            data+=teamName+","+playerDetails[0].text+","+playerDetails[1].text+","+playerDetails[3].text+",\n"
        except:
            data+=teamName+",-,-,-,\n"
        #print(data)
        fl.write(data)
        driver.back()
        length="window.scrollTo(0,"+str(i*50+100)+")"
        driver.execute_script(length)
                                          
fl.close()
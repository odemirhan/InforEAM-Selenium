from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys as keys
import pandas as pd
import os
import time

def searchanddelete(inputasstr):
    
    inp=inputasstr
   
    
    print(inp)
    try:
        wait.until(lambda driver: driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr"))
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr")))
        elem03=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr")

        driver.execute_script("arguments[0].click();", elem03)

        time.sleep(5)
                


        wait.until(lambda driver: driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div/div/button[2]"))
        elem05=driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div/div/button[2]")

        driver.execute_script("arguments[0].click();", elem05)

        time.sleep(5)
        elem01=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/table/thead/tr[3]/th[21]/input")




        driver.execute_script("arguments[0].click();", elem01)
        elem01.send_keys(keys.CONTROL, "a")
        elem01.send_keys(keys.BACKSPACE)
    except:
        elem01=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/table/thead/tr[3]/th[21]/input")
        driver.execute_script("arguments[0].click();", elem01)
        elem01.send_keys(keys.CONTROL, "a")
        elem01.send_keys(keys.BACKSPACE)
           

def checkifexists(inputasstr):
    inp=inputasstr
    wait.until(lambda driver: driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/table/thead/tr[3]/th[21]/input'))
      

    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/table/thead/tr[3]/th[21]/input")))

    elem01=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/table/thead/tr[3]/th[21]/input")



    driver.execute_script("arguments[0].click();", elem01)
    elem01.send_keys(inp)
    elem01.send_keys(keys.RETURN)

    try:
        wait.until(lambda driver: driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr"))
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr")))
        elem03=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/table/tbody/tr")
        print("trueee")
        return True

    except:
        elem01=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/table/thead/tr[3]/th[21]/input")
        driver.execute_script("arguments[0].click();", elem01)
        elem01.send_keys(keys.CONTROL, "a")
        elem01.send_keys(keys.BACKSPACE)
        
        return False

driver= webdriver.Chrome()


wait=WebDriverWait(driver,7)


DF=pd.read_excel('LV.xlsx')

aaa=input("gir")
#wait.until(lambda driver: driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/iframe'))

iframeaa=driver.find_elements_by_xpath('//iframe')
driver.switch_to.frame(iframeaa[0])


#iframe1=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div[3]/div[3]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/iframe')
#driver.switch_to.frame(iframe1)



#wait.until(lambda driver: driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div[3]/div/div/div/div[4]/div/div/div[2]/div[2]/div/div[1]/div[1]/iframe'))

iframebb=driver.find_elements_by_xpath('//iframe')
driver.switch_to.frame(iframebb[0])

#iframe=driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div[3]/div/div/div/div[4]/div/div/div[2]/div[2]/div/div[1]/div[1]/iframe')
#driver.switch_to.frame(iframe)



driver.execute_script("document.body.style.zoom='50%'")

for cntDF in range(len(DF)):
    iii=0
    while iii<3:
        if checkifexists(str(DF.iat[cntDF, 0])):
            searchanddelete(str(DF.iat[cntDF, 0]))
            if not checkifexists(str(DF.iat[cntDF, 0])):
                break
            else:
                iii+=1
        else:
            print("selam")
            break
                
                                 
                        
       
    
   

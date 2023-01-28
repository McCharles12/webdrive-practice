
import time
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
#from selenium.webdriver.common.action_chains import ActionChains
import logging


logging.basicConfig(filename='eggsample.log', encoding='utf-8', level=logging.INFO, 
format='%(levelname)s %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

currTime = time.strftime("%D-%H:%M:%S", time.localtime())
#By.ID, 'searchInput'

driver = webdriver.Chrome()
driver.implicitly_wait(5)
achain = ActionChains(driver)

#This function opens the browser, maximizes the window, and opens the CCTB website.
def openCCTB():
    logging.info('- Opening browser.')
        
    driver.maximize_window()
    print('\nOpening browser at: ', currTime)

    driver.get("https://www.canadianctb.ca/")
    logging.info('- Successfully opened www.canadianctb.ca.')

    print('\nYou have arrived at ', driver.title)

def screenshooter():
    #driver.get_screenshot_as_file("C:\\Users\\cgmcc\\Documents\\zzxzz.png")
    driver.save_screenshot("C:\\Users\\cgmcc\\Documents\\zzxz.png")

def hovercraft():
   hover = driver.find_element(By.XPATH, "/html/body/nav[2]/div[2]/div/ul[2]/li[2]")
   skedule = driver.find_element(By.XPATH, '//*[@id="navbarCollapse"]/ul[2]/li[2]/ul/li[5]/a')
   achain.move_to_element(hover).click(skedule).perform()
   

#This function clicks the link to CCTB Virtual Student Lounge and ascertains the desired URL and Title.
def clikit():   
    lounge = driver.find_element(By.XPATH, '/html/body/nav[2]/div[2]/div/ul[1]/li[2]/a')
    lounge.click()
    logging.info('- Clicked Link to Virtual Student lounge -') 
    if driver.current_url == "https://www.canadianctb.ca/virtual-student-lounge" and driver.title == "Virtual Student Lounge | CCTB":
        driver.save_screenshot("C:\\Users\\cgmcc\\Documents\\zzxz.png")
        logging.info(" - Successfully arrived at destination")
        print("\nThis is the url for CCTB's student lounge:", driver.current_url, "\n")
        print("This is the page's title: ", driver.title, '\n')
    else:
        logging.warning(" - Something Has gone wrong. Review the code.")
        print('WHAT IS HAPPENINGGGG?!?!?!\n')
    

#Calling the Functions

openCCTB()
time.sleep(1)



#hovercraft()
#time.sleep(2)


clikit()
time.sleep(1)

driver.close()
logging.info('- Closed Browser.')

print('The test was completed at: ', currTime)

driver.quit()


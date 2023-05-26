import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
username ="*********"
accessToken ="****"
passs="********"
gridUrl = "hub.lambdatest.com/wd/hub"
url = "https://"+username+":"+accessToken+"@"+gridUrl
@pytest.mark.parallel #---> This is the command which is used to run parallel testing
def test_search():
    capability_1= {
        "browserName": "Chrome",
        "browserVersion": "114.0",
        "LT:Options": {
            "platformName": "Windows 11",
            "project": "Untitled_1"
        }
    }
    driver_1 = webdriver.Remote(
        command_executor=url,
        desired_capabilities=capability_1
    )
    driver_1.get("https://accounts.lambdatest.com/login")
    driver_1.find_element("id","email").send_keys(username)
    driver_1.find_element("id","password").send_keys(passs)
    #driver.find_element("id","login-button").click()
    elem = driver_1.find_element("id","email")
    elem.send_keys("https://accounts.lambdatest.com/login")
    elem.submit()
    driver_1.find_element("id","login-button").click()
    print("Printing title of current page :"+driver_1.title)
    driver_1.execute_script("lambda-status=passed")
    print("Requesting to mark test : pass")
    driver_1.quit()
@pytest.mark.parallel #This is the the command which is used to run prallel testing
def test_para():
    capability_2= {
        "browserName": "Chrome",
        "browserVersion": "114.0",
        "LT:Options": {
            "platformName": "Windows 10",
            "project": "Untitled_1"
        }
    }
    driver_2= webdriver.Remote(
        command_executor=url,
        desired_capabilities=capability_2
    )
    driver_2.get("https://accounts.lambdatest.com/login")
    driver_2.find_element("id","email").send_keys(username)
    driver_2.find_element("id","password").send_keys(passs)
    #driver.find_element("id","login-button").click()
    elem = driver_2.find_element("id","email")
    elem.send_keys("https://accounts.lambdatest.com/login")
    elem.submit()
    driver_2.find_element("id","login-button").click()
    print("Printing title of current page :"+driver_2.title)
    driver_2.execute_script("lambda-status=passed")
    print("Requesting to mark test : pass")
    driver_2.quit()
@pytest.mark.parallel #This is the the command which is used to run prallel testing
def test_para1():
    capability_2= {
        "browserName": "MicrosoftEdge",
        "browserVersion": "112.0",
        "LT:Options": {
            "platformName": "Windows 10",
            "project": "Untitled_1"
        }
    }
    driver_2= webdriver.Remote(
        command_executor=url,
        desired_capabilities=capability_2
    )
    driver_2.get("https://accounts.lambdatest.com/login")
    driver_2.find_element("id","email").send_keys(username)
    driver_2.find_element("id","password").send_keys(passs)
    #driver.find_element("id","login-button").click()
    elem = driver_2.find_element("id","email")
    elem.send_keys("https://accounts.lambdatest.com/login")
    elem.submit()
    driver_2.find_element("id","login-button").click()
    print("Printing title of current page :"+driver_2.title)
    driver_2.execute_script("lambda-status=passed")
    print("Requesting to mark test : pass")
    driver_2.quit()
#Bascially hum n number of functions bana rahe he unk alag alag capabilites ke hisab se sset kar rahe he
#One Thing to note is that function name should be different
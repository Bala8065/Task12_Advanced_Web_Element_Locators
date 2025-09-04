import pytest
from pyautogui import click
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup for Selenium WebDriver
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
# Relative xpath for Course
def test_course(setup):
    driver = setup
    driver.get("https://www.guvi.in/")  #Guvi website
    (driver.find_element(By.XPATH,"//a[@class='⭐️rwl3jt-0 my-2 cursor-pointer ml-2 mr-6 text-base font-normal text-gray-500 text-nowrap']")
     .click())
    time.sleep(3)
    url = driver.current_url
    assert url == "https://www.guvi.in/courses/?current_tab=paidcourse"  # Expected URL
    title = driver.title
    assert title == "GUVI | courses"

# Relative xpath for Live classes
def test_Liveclasses(setup):
    driver = setup
    driver.get("https://www.guvi.in/")  ##Guvi website
    (driver.find_element(By.XPATH,"//p[@id='liveclasseslink']").click())
    time.sleep(3)
    url = driver.current_url
    assert url == "https://www.guvi.in/"  # Expected URL
    title = driver.title
    assert title == "GUVI | Learn to code in your native language"

#Relative xpath for Partice
def test_practice (setup):
    driver = setup
    driver.get("https://www.guvi.in/")  ##Guvi website
    (driver.find_element(By.XPATH,"//p[@id='practiceslink']").click())
    time.sleep(3)
    url = driver.current_url
    assert url == "https://www.guvi.in/"  # Expected URL
    title = driver.title
    assert title == "GUVI | Learn to code in your native language"

#Relative xpath for Resource
def test_Resource (setup):
    driver = setup
    driver.get("https://www.guvi.in/")  ##Guvi website
    (driver.find_element(By.XPATH,"//p[@id='resourceslink']").click())
    time.sleep(3)
    url = driver.current_url
    assert url == "https://www.guvi.in/"  # Expected URL
    title = driver.title
    assert title == "GUVI | Learn to code in your native language"

#Relative xpath for Prodcuts
def test_products (setup):
    driver = setup
    driver.get("https://www.guvi.in/")  ##Guvi website
    (driver.find_element(By.XPATH,"//p[@id='solutionslink']").click())
    time.sleep(3)
    url = driver.current_url
    assert url == "https://www.guvi.in/"  # Expected URL
    title = driver.title
    assert title == "GUVI | Learn to code in your native language"

#Relative xpath for Login
def test_Login (setup):
    driver = setup
    driver.get("https://www.guvi.in/")  ##Guvi website
    (driver.find_element(By.XPATH,"//a[@id='login-btn']").click())
    time.sleep(3)
    url = driver.current_url
    assert url == "https://www.guvi.in/sign-in/"  # Expected URL
    title = driver.title
    assert title == "GUVI | Login"

#Relative xpath for Signup
def test_signup (setup):
    driver = setup
    driver.get("https://www.guvi.in/")  ##Guvi website
    (driver.find_element(By.XPATH,"//a[@class='⭐️rawbli-0 bg-green-500 hover:bg-green-600 text-white font-normal"
                                  " py-2 px-4 rounded text-base min-h-8 h-8 align-middle mr-2 text-nowrap']").click())
    time.sleep(3)
    url = driver.current_url
    assert url == "https://www.guvi.in/register/"  # Expected URL
    title = driver.title
    assert title == "GUVI | Sign Up"

#First child element for
def test_firstchildelement(setup):
    driver = setup
    driver.get("https://www.guvi.in/")  ##Guvi website
    #Liveclass child
    (driver.find_element(By.XPATH,"//div[@class='⭐️rwl3jt-0 hidden lg:flex basis-auto']/child::div[1]").click())

    # Partice child
    (driver.find_element(By.XPATH, "//div[@class='⭐️rwl3jt-0 hidden lg:flex basis-auto']/child::div[2]").click())

    # Resource child
    (driver.find_element(By.XPATH, "//div[@class='⭐️rwl3jt-0 hidden lg:flex basis-auto']/child::div[3]").click())

    # Products child
    (driver.find_element(By.XPATH, "//div[@class='⭐️rwl3jt-0 hidden lg:flex basis-auto']/child::div[4]").click())

    time.sleep(3)
    url = driver.current_url
    assert url == "https://www.guvi.in/"  # Expected URL
    title = driver.title
    assert title == "GUVI | Learn to code in your native language"


#Second sibling child element for Live classes_sibiling child- 1
def test_Liveclass_second_sibling_1 (setup):
    driver = setup
    driver.get("https://www.guvi.in/")  ##Guvi website
    (driver.find_element(By.XPATH,"//p[@id='liveclasseslink']").click())

    # Adjust wait as needed
    driver.implicitly_wait(10)
    # Find the second sibling of "Courses"

    driver.find_element(By.XPATH, "//li[@class='⭐️rwl3jt-0 mt-2']//following-sibling::li[1]").click()
    time.sleep(3)
    url = driver.current_url
    assert url == "https://www.guvi.in/zen-class/full-stack-development-course/"  # Expected URL
    title = driver.title
    assert title == "Full Stack Development Course With Placement | Zen Class | GUVI"

#Second sibling child element for Live classes_sibiling child- 2
def test_Liveclass_second_sibling_2 (setup):
    driver = setup
    driver.get("https://www.guvi.in/")  ##Guvi website
    (driver.find_element(By.XPATH,"//p[@id='liveclasseslink']").click())

    # Adjust wait as needed
    driver.implicitly_wait(10)
    # Find the second sibling of "Courses"

    driver.find_element(By.XPATH, "//li[@class='⭐️rwl3jt-0 mt-2']//following-sibling::li[2]").click()
    time.sleep(3)
    url = driver.current_url
    assert url == "https://www.guvi.in/zen-class/data-science-course/"  # Expected URL
    title = driver.title
    assert title == "Data Science Course With Placement | Zen Class | GUVI"

def test_Liveclass_second_sibling_3 (setup):
    driver = setup
    driver.get("https://www.guvi.in/")  ##Guvi website
    (driver.find_element(By.XPATH,"//p[@id='liveclasseslink']").click())

    # Adjust wait as needed
    driver.implicitly_wait(10)
    # Find the second sibling of "Courses"

    driver.find_element(By.XPATH, "//li[@class='⭐️rwl3jt-0 mt-2']//following-sibling::li[3]").click()
    time.sleep(3)
    url = driver.current_url
    assert url == "https://www.guvi.in/zen-class/selenium-automation-testing-course/"  # Expected URL
    title = driver.title
    assert title == "GUVI | Automation Testing With Selenium"

def test_Liveclass_second_sibling_4 (setup):
    driver = setup
    driver.get("https://www.guvi.in/")  ##Guvi website
    (driver.find_element(By.XPATH,"//p[@id='liveclasseslink']").click())

    # Adjust wait as needed
    driver.implicitly_wait(10)
    # Find the second sibling of "Courses"

    driver.find_element(By.XPATH, "//li[@class='⭐️rwl3jt-0 mt-2']//following-sibling::li[4]").click()
    time.sleep(3)
    url = driver.current_url
    assert url == "https://www.guvi.in/zen-class/"  # Expected URL
    title = driver.title
    assert title == "Zen Class - Career Programs from GUVI"

# Parent element parent element of an element with the attribute href - Resource module
def test_practice_module_parent_element_href(setup):
    driver = setup
    driver.get("https://www.guvi.in/")

    # Click the "Practice" link by ID
    driver.find_element(By.ID, "resourceslink").click()

    # Wait to ensure the element is loaded
    driver.implicitly_wait(10)

    # Click the "CodeKata" link using href
    driver.find_element(By.XPATH, "//a[@class='⭐️rwl3jt-0' and contains(@href, '/zen-class-review/')]").click()
    time.sleep(3)
    url = driver.current_url
    assert url == "https://www.guvi.in/zen-class-review/"  # Expected URL
    title = driver.title
    assert title == "GUVI - Zen Class Success Stories"

#Xpath-Axes
def test_practice_module_Axex_anscetor(setup):
    driver = setup
    driver.get("https://www.guvi.in/")

    # # Click the "Practice" link by ID
    # driver.find_element(By.ID, "resourceslink").click()
    #
    # # Wait to ensure the element is loaded
    driver.implicitly_wait(10)

    # Click the "CodeKata" link using href
    driver.find_element(By.XPATH, "//a[@class='⭐️rwl3jt-0 flex flex-col items-start text-primary text-base leading-7 py-3.5 exploreBtnMobile']/ancestor::*[1]").click()
    time.sleep(3)
    url = driver.current_url
    assert url == "https://www.guvi.in/zen-class-review/"  # Expected URL
    title = driver.title
    assert title == "GUVI - Zen Class Success Stories"


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_gmail_login():
    #launch Chrome browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open HTML login page
    driver.get(
        "file:///C:/Users/admin/PycharmProjects/PythonProject/login.html"
    )


    #maximize browser
    driver.maximize_window()

    #wait object
    wait=WebDriverWait(driver, 60)

    print("login page opened")
    # Open new tab
    #@driver.switch_to.new_window('tab')

    # Open Google in new tab
    #@driver.get("https://www.google.com")

    #@print("Google opened in new tab")

    #time.sleep(3)

    # Get all window handles
    #@windows = driver.window_handles

    # Switch back to first tab (login page)
    #@driver.switch_to.window(windows[0])

    #@print("Switched back to login page")

    #locate email field
    email = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    #email_text=driver.find_element(By.ID,"email")
    #email_text.send_keys("lingampallisreenitha@gmail.com")
    #password=driver.find_element(By.ID,"password")
    #password.send_keys("Sree@2002")
    #driver.find_element(By.ID,"signin").click()


    #wait for password field
    password = wait.until(EC.visibility_of_element_located((By.ID,"password")))

    print("please enter email and password")
    print("Then click Sign In button")
    # Wait until success message appears
    wait.until(
        EC.text_to_be_present_in_element(
            (By.ID, "success"),
            "Login Successful"
        )
    )

    # time.sleep(15).

    # Locate Sign In button
    #signin_button = wait.until(EC.element_to_be_clickable((By.ID, "signin")))

    # Click Sign In button
    #signin_button.click()





    # Verify success message
    assert "Login Successful" in driver.page_source

    print("Login successful verified")
    time.sleep(5)
    #close browser
    driver.quit()
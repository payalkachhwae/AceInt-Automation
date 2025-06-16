import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ---------- Pytest Fixture to manage WebDriver ----------
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# ---------- Pytest Test Case ----------
def test_start_interview(driver):
    # Step 1: Open Login Page
    driver.get("https://demo.aceint.ai/auth/signin")

    # Step 2: Log In
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[1]/input").send_keys("kachhwaepayal@gmail.com")
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[2]/div[1]/input").send_keys("123456789")
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/button").click()
    time.sleep(1)

    # Step 3: Go to Home Page
    driver.get("https://demo.aceint.ai/")
    time.sleep(1)

    # Step 4: Click "Practice Interview" Button
    practice_btn = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/button/div")
    practice_btn.click()
    time.sleep(2)  # Wait for the form to load

    # Step 5: Select Job Role
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div/div[1]/label[1]/select/option[6]").click()
    # driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/form/label[1]/select/option[6]").click()

    # Step 6: Select Interview Type
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div/div[1]/label[2]/select/option[2]").click()

    # Step 7: Select Duration
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div/div[2]/label[1]/select/option[1]").click()

    # Step 8: Select Difficulty
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div/div[2]/label[2]/select/option[1]").click()

    # Step 9: Enter Technical Skill
    skill_input = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div/div[3]/label/div/div[2]/span[10]").click()
    # skill_input.send_keys("Python")
    # skill_input.send_keys(Keys.ENTER)
    time.sleep(1)

    # Step 10: Agree to Terms
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[2]/div/div[1]/label/button").click()
    time.sleep(1)

    # Step 11: Start Interview
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[2]/div/div[2]/button").click()
    time.sleep(30)

    # Step 12: Click Start Interview on Final Page
    driver.find_element(By.XPATH, "/html/body/div/main/div/section[2]/div/div[2]/a").click()
    time.sleep(25)

    # Step 13: Validate Result
    assert "interview" in driver.current_url

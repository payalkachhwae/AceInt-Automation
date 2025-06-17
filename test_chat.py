import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ---------- Fixture to set up and tear down the Chrome WebDriver ----------
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# ---------- Pytest test case ----------
def test_chat_input_submission(driver):
    driver.get("https://demo.aceint.ai/auth/signin")
    
    # --- Login ---
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[1]/input").send_keys("kachhwaepayal@gmail.com")
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[2]/div[1]/input").send_keys("123456789")
    driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/button").click()
    
    # --- Wait for redirection to chat page ---
    time.sleep(3)
    
    # --- First Message in Chat: "Python" ---
    input_box = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div/div/main/div/div/div[2]/form/textarea")
    input_box.send_keys("Python")
    
    send_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div/div/main/div/div/div[2]/form/div/div[2]/button")
    send_button.click()
    
    # --- Wait for response to appear ---
    time.sleep(20)  # Adjust based on how long the model takes to respond
    
    # --- Second Message: "Give me guide on..." ---
    input_box = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div/div/div[3]/div/div/form/textarea")
    input_box.clear()
    input_box.send_keys("Give me guide on interview")

    send_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div/div/div[3]/div/div/form/div/div[2]/button")
    send_button.click()

    # --- Wait to observe the second response ---
    time.sleep(20)

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
    
    # --- Enter message in chat input ---
    input_box = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div/div/main/div/div/div[2]/form/textarea")
    input_box.send_keys("Python")
    
    # --- Click send button ---
    send_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/main/div/div/div/main/div/div/div[2]/form/div/div[2]/button")
    send_button.click()
    
    # --- Wait to observe the response or message echo ---
    time.sleep(20)

    # You can optionally assert the presence of the sent message or response later
    # Example: assert "Guide me how to give interview" in driver.page_source

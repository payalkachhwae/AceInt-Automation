import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demo.aceint.ai/auth/signin")
    yield driver
    driver.quit()

def test_submit_feedback(driver):
    wait = WebDriverWait(driver, 20)

    # --- LOGIN ---
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys("kachhwaepayal@gmail.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456789")
    driver.find_element(By.XPATH, "//button[text()='Sign In']").click()

    # --- FEEDBACK BUTTON ---
    feedback_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Feedback']]")))
    feedback_btn.click()

    # --- TEXTAREA ---
    feedback_textarea = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/textarea")))
    feedback_textarea.clear()
    feedback_textarea.send_keys("Great experience! Very interactive and realistic AI interview.")

    # --- WAIT FOR STARS CONTAINER ---
    stars_container = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[3]")))

    # --- CLICK 4TH STAR ---
    stars = stars_container.find_elements(By.XPATH, ".//button")
    if len(stars) >= 4:
        try:
            stars[3].click()
        except Exception as e:
            time.sleep(1)
            stars[3].click()
    else:
        raise Exception("Less than 4 stars found!")

    # --- SUBMIT FEEDBACK ---
    submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[4]/button")))
    submit_btn.click()

    # --- OPTIONAL: Wait for success or confirmation ---
    time.sleep(2)  # replace with a proper success message check if available

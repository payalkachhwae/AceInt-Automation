import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_extract_full_feedback(driver):
    # Step 1: Login
    driver.get("https://demo.aceint.ai/auth/signin")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    ).send_keys("fagema3509@jio1.com")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
    ).send_keys("Pass@12345")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/form/button"))
    ).click()

    time.sleep(10)

    # Step 2: Construct URL with session ID and current time
    session_id = "d685cf22-46dc-45d3-9fc3-40adb371f99b"
    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    feedback_url = f"https://demo.aceint.ai/interview/summary/{session_id}?time={timestamp}"
    driver.get(feedback_url)

    # Step 3: Wait for the feedback page to load
    time.sleep(10)  # Use longer wait if needed

    # Step 4: Extract feedback values

    try:
        overall_score = driver.find_element(By.XPATH, "//div[contains(text(),'Overall Score')]/following-sibling::div").text
        campus_status = driver.find_element(By.XPATH, "//div[contains(text(),'Campus Readiness')]/following-sibling::div").text
        tech_readiness = driver.find_element(By.XPATH, "//div[contains(text(),'Technical Readiness')]/following-sibling::div").text
        comm_readiness = driver.find_element(By.XPATH, "//div[contains(text(),'Communication Readiness')]/following-sibling::div").text
        confidence = driver.find_element(By.XPATH, "//div[contains(text(),'Confidence Level')]/following-sibling::div").text
        tech_score = driver.find_element(By.XPATH, "//div[contains(text(),'Technical Knowledge')]/following-sibling::div//div[contains(text(),'/10')]").text
        tech_status = driver.find_element(By.XPATH, "//div[contains(text(),'Technical Knowledge')]/following-sibling::div[contains(text(),'Below Average') or contains(text(),'Good')]").text

        print("\n🔍 Interview Feedback Extracted:")
        print(f"⭐ Overall Score: {overall_score}")
        print(f"🎯 Campus Readiness: {campus_status}")
        print(f"💻 Technical Readiness: {tech_readiness}")
        print(f"🗣️ Communication Readiness: {comm_readiness}")
        print(f"🔒 Confidence Level: {confidence}")
        print(f"📊 Technical Knowledge Score: {tech_score} ({tech_status})")

        time.sleep(10)
    
    except Exception as e:
        print("⚠️ Failed to extract one or more feedback elements:", e)

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_resume_flow_simple(driver):
    driver.get("https://demo.aceint.ai/auth/signin")
    wait = WebDriverWait(driver, 30)

    # --- Login ---
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys("kachhwaepayal@gmail.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456789")
    driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
    print("✅ Logged in.")

    # # --- Wait for Dashboard to Load ---
    # wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Dashboard') or contains(text(), 'Welcome')]")))
    # print("🟢 Dashboard loaded.")

    # --- Click Resume Upload Card ---
    resume_card = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/main/div/div/div/main/div/div/div[1]/div[2]/div/div[1]/div/div/div")))
    resume_card.click()
    print("📄 Resume card clicked.")

    # # --- Wait for Modal/Form ---
    # wait.until(EC.visibility_of_element_located((By.XPATH, "//form")))
    # print("🟢 Modal loaded.")

    # --- Open Interview Type Dropdown ---
    dropdown_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/form/div[1]/div/button")))
    dropdown_button.click()
    print("⬇️ Interview type dropdown opened.")
    time.sleep(2)

    # --- Click on 'Technical' Option ---
    technical_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option' and normalize-space()='Technical']")))
    technical_option.click()
    print("✅ 'Technical' interview type selected.")
    time.sleep(2)

    # --- Select 10 Min Radio Button ---
    wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'10 Min')]"))).click()
    print("⏱️ Duration '10 Min' selected.")

    # --- Upload Resume ---
    upload_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    upload_input.send_keys("C:/Users/hp/Downloads/PayalKachhwae_DataAnalyst_Resume.pdf")
    print("📁 Resume uploaded.")
    time.sleep(5)

    # --- Click Start Interview ---
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/form/button"))).click()
    print("🚀 Interview started...")

    # --- Final URL Check ---
    time.sleep(5)
    assert "interview" in driver.current_url.lower()
    print("✅ Interview page loaded successfully.")

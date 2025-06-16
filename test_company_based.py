import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_company_based_interview(driver):
    driver.get("https://demo.aceint.ai/auth/signin")
    wait = WebDriverWait(driver, 30)

    # --- Login ---
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys("kachhwaepayal@gmail.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456789")
    driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
    print("✅ Logged in.")

    # --- Click Company-Based Interview Card ---
    company_card = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/main/div/div/div/main/div/div/div[1]/div[2]/div/div[2]/div/div/div")))
    company_card.click()
    print("📄 Company-Based Interview card clicked.")

    # --- Fill Company Name ---
    company_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Accenture, Uber, etc.']")))
    company_input.send_keys("Amazon")
    print("🏢 Company name entered.")

    time.sleep(3)  # Wait briefly for animations

    # # --- Wait for overlay to disappear ---
    # try:
    #     WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='fixed inset-0 z-50 bg-black/80 data-[state=open]:animate-in']")))
    # except:
    #     print("⚠️ Overlay might already be gone.")

    # --- Select Interview Domain ---
    domain_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/form/div[2]/div[1]/button")))
    try:
        domain_dropdown.click()
    except:
        driver.execute_script("arguments[0].click();", domain_dropdown)
    print("🔽 Domain dropdown clicked.")

    domain_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option' and normalize-space()='Service Based Company']")))
    domain_option.click()
    print("💻 Interview domain selected.")

    # --- Select Interview Type ---
    type_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/form/div[2]/div[2]/div/button")))
    try:
        type_dropdown.click()
    except:
        driver.execute_script("arguments[0].click();", type_dropdown)
    print("🔽 Type dropdown clicked.")

    type_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option' and normalize-space()='Technical']")))
    type_option.click()
    print("🎯 Interview type selected.")

    # --- Select Duration ---
    wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'10 Mins')]"))).click()
    print("⏱️ 10 mins selected.")

    # --- Upload Resume ---
    upload_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    resume_path = os.path.abspath("C:/Users/hp/Downloads/PayalKachhwae_DataAnalyst_Resume.pdf")
    upload_input.send_keys(resume_path)
    print("📁 Resume uploaded.")

    # --- Click Start Interview ---
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Start Interview')]"))).click()
    print("🚀 Interview started...")

    time.sleep(5)
    assert "interview" in driver.current_url.lower()
    print("✅ Interview page successfully loaded.")

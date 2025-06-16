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

def test_custom_job_role_resume_upload(driver):
    driver.get("https://demo.aceint.ai/auth/signin")
    wait = WebDriverWait(driver, 20)

    # --- Login ---
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys("kachhwaepayal@gmail.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456789")
    driver.find_element(By.XPATH, "//button[text()='Sign In']").click()
    print("✅ Logged in")

    # --- Click the Resume Card (Job Role Based Interview) ---
    resume_card = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/main/div/div/div/main/div/div/div[1]/div[2]/div/div[3]/div/div/div")))
    resume_card.click()
    print("📄 Job Role card clicked")

    # # --- Wait for Modal ---
    # wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Job Role Based Interview')]")))
    # print("🟢 Modal loaded")

    # --- Type into Job Role Field ---
    job_role_input = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/form/div[1]/div[1]/input")))
    job_role_input.clear()
    job_role_input.send_keys("Software Developer")
    print("💼 Typed job role")

    # --- Select Interview Type ---
    interview_type_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/form/div[1]/div[2]/div/button")))
    interview_type_btn.click()

    time.sleep(3)

    technical_option_xpath = "//div[@role='option' and normalize-space()='Technical']"
    technical_option = wait.until(EC.element_to_be_clickable((By.XPATH, technical_option_xpath)))
    try:
        technical_option.click()
        time.sleep(3)

    except:
        driver.execute_script("arguments[0].click();", technical_option)
    print("🧪 Interview type 'Technical' selected")

    # --- Fill Job Description ---
    description_input = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/form/div[2]/textarea")))
    description_input.clear()
    description_input.send_keys("Responsible for developing scalable web applications, collaborating with cross-functional teams, and ensuring code quality.")
    print("📝 Job description entered")

    # --- Select Duration ---
    radio_10min = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'10 Min')]")))
    radio_10min.click()
    print("⏱️ 10 Min duration selected")

    # # --- Upload Resume ---
    # file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    # file_input.send_keys("C:/Users/hp/Downloads/Payal_Resume.pdf")
    # print("📁 Resume uploaded")

    # --- Click Start Interview ---
    start_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/form/button")))
    start_btn.click()
    print("🚀 Interview started")

    # --- Final Check ---
    time.sleep(5)
    assert "interview" in driver.current_url.lower()
    print("✅ Interview page loaded successfully")

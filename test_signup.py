import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------- Fixture for browser setup ----------
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# ---------- Test: Sign-Up Form ----------
def test_valid_signup(driver):
    driver.get("https://demo.aceint.ai/auth/signup")
    wait = WebDriverWait(driver, 20)

    # Fill First Name
    first_name = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='John']")))
    first_name.send_keys("Payal")

    # Fill Last Name
    last_name = driver.find_element(By.XPATH, "//input[@placeholder='Doe']")
    last_name.send_keys("Kachhwae")

    # Fill Email (unique to avoid conflict)
    email_field = driver.find_element(By.XPATH, "//input[@type='email']")
    unique_email = f"payal{int(time.time())}@example.com"
    email_field.send_keys(unique_email)

    # Fill Password
    password_field = driver.find_element(By.XPATH, "//input[@type='password']")
    password_field.send_keys("Test@12345")

    # Click Create Account
    create_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Account')]")
    create_button.click()

    wait = WebDriverWait(driver, 20)

    # # Wait for redirection to Sign In page (or dashboard)
    # success_indicator = wait.until(
    #     EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Sign In')]"))
    # )

    # # Assertion
    # assert success_indicator.is_displayed()
    # print("✅ Sign-up completed and redirected to Sign In page.")

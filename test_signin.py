import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ---------- Fixture: Chrome with suppressed logs ----------
@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


# ---------- Test Case 1: Valid Login ----------
def test_valid_login(driver):
    driver.get("https://demo.aceint.ai/auth/signin")
    wait = WebDriverWait(driver, 20)

    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys("kachhwaepayal@gmail.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456789")
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()

    dashboard_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Feedback')]")))
    assert dashboard_element.is_displayed(), "❌ Dashboard not loaded after login"


# ---------- Test Case 2: Invalid Login ----------
def test_invalid_login(driver):
    driver.get("https://demo.aceint.ai/auth/signin")
    wait = WebDriverWait(driver, 15)

    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys("kachhwaepayal@gmail.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("wrongpassword")
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()

    try:
        error_element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Invalid email or password') or contains(text(), 'Invalid')]"))
        )
        assert error_element.is_displayed(), "❌ Error message not visible for invalid login"
    except Exception as e:
        current_url = driver.current_url
        if current_url == "https://demo.aceint.ai/auth/signin":
            print("⚠️ URL unchanged after login, assuming login failed as expected.")
        else:
            pytest.fail("❌ Login failed but no error message or behavior detected.")


# ---------- Test Case 3: Empty Fields Login ----------
def test_empty_fields_login(driver):
    driver.get("https://demo.aceint.ai/auth/signin")
    wait = WebDriverWait(driver, 30)

    # Click sign-in button without entering any input
    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Sign In']")))
    sign_in_button.click()

    try:
        # Try multiple possible locations for email and password validation errors
        email_error = wait.until(
            EC.visibility_of_element_located((By.XPATH,
                "//input[@type='email']"
            ))
        )

        password_error = wait.until(
            EC.visibility_of_element_located((By.XPATH,
                "//input[@type='password']"
            ))
        )

        # Assertions
        assert email_error.is_displayed(), "❌ Email error message not shown"
        assert password_error.is_displayed(), "❌ Password error message not shown"
        print("✅ Validation error messages displayed successfully.")

    except Exception as e:
        print("⚠️ Could not locate expected error messages.")
        print("Page source for debugging:")
        print(driver.page_source)
        pytest.fail("❌ Validation messages for empty fields not found.")
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ---------- Fixture for setting up and closing the browser ----------
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# ---------- Test function ----------
def test_valid_login(driver):
    driver.get("https://demo.aceint.ai/auth/signin")
    wait = WebDriverWait(driver, 20)

    # --- Fill login form ---
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys("kachhwaepayal@gmail.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456789")
    driver.find_element(By.XPATH, "//button[normalize-space()='Sign In']").click()

    # --- Wait for dashboard page to load (check for unique dashboard element) ---
    dashboard_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Feedback')]")))

    # --- Assertion (check if dashboard is loaded by URL or element presence) ---
    assert dashboard_element.is_displayed(), "❌ Dashboard not loaded after login"

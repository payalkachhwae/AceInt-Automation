import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    # Setup
    driver = webdriver.Chrome()
    driver.get("https://demo.aceint.ai/auth/signin")
    yield driver
    # Teardown
    driver.quit()

def get_current_mode(driver):
    html_tag = driver.find_element(By.TAG_NAME, "html")
    class_value = html_tag.get_attribute("class")
    return "dark" if "dark" in class_value else "light"

def test_toggle_dark_light_mode(driver):
    wait = WebDriverWait(driver, 20)

    # --- Login ---
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys("kachhwaepayal@gmail.com")
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456789")
    driver.find_element(By.XPATH, "//button[text()='Sign In']").click()

    # Wait for dashboard to load
    time.sleep(10)

    # --- Toggle Mode ---
    toggle_xpath = "/html/body/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/button"

    # Check current mode
    initial_mode = get_current_mode(driver)
    print(f"Initial Mode: {initial_mode}")

    # Click toggle
    toggle_btn = wait.until(EC.element_to_be_clickable((By.XPATH, toggle_xpath)))
    toggle_btn.click()
    time.sleep(3)

    # Verify new mode
    new_mode = get_current_mode(driver)
    print(f"✅ Switched to {new_mode.capitalize()} Mode")
    assert new_mode != initial_mode, "Mode did not change after first toggle"

    # Toggle back
    toggle_btn = wait.until(EC.element_to_be_clickable((By.XPATH, toggle_xpath)))
    toggle_btn.click()
    time.sleep(3)

    final_mode = get_current_mode(driver)
    print(f"✅ Switched back to {final_mode.capitalize()} Mode")
    assert final_mode == initial_mode, "Mode did not revert after second toggle"

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# open the browser
driver = webdriver.Chrome(ChromeDriverManager().install())

# open the site
driver.get("https://orteil.dashnet.org/cookieclicker/")

# wait loading
time.sleep(5)

# accept the cookies
accept_cookies = driver.find_element(By.CSS_SELECTOR, ".cc_btn.cc_btn_accept_all")
accept_cookies.click()

# select a language
select_language = driver.find_element(By.CSS_SELECTOR, "#langSelect-PT-BR")
select_language.click()

# wait loading
time.sleep(5)

# click in the big cookie
select_big_cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")
while True:
    select_big_cookie.click()

    # golden_cookie = driver.find_element(By.CSS_SELECTOR, ".goldenCookie")

    features = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")
    features[-1].click() if features else None

    upgrades = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
    upgrades[-1].click() if upgrades else None

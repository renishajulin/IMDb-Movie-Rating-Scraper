import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def setup_browser(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrape_imdb_top_250():
    url = "https://www.imdb.com/chart/top/"
    driver = setup_browser(headless=False)  

    print("[INFO] Loading IMDb Top 250 page...")
    driver.get(url)

    WebDriverWait(driver, 4).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ipc-metadata-list-summary-item"))
    )

    movie_rows = driver.find_elements(By.CSS_SELECTOR, ".ipc-metadata-list-summary-item")
    movies = []

    for index, row in enumerate(movie_rows, start=1):
        try:
            title = row.find_element(By.CSS_SELECTOR, "h3").text
            year = row.find_element(By.CSS_SELECTOR, ".cli-title-metadata-item:nth-child(1)").text
            rating = row.find_element(By.CSS_SELECTOR, ".ipc-rating-star--imdb .ipc-rating-star--rating").text

            movies.append({
                "Rank": index,
                "Title": title,
                "Year": year,
                "IMDb Rating": rating
            })
        except Exception as e:
            print(f"[WARNING] Skipped a row due to error: {e}")

    driver.quit()
    return pd.DataFrame(movies)

if __name__ == "__main__":
    df = scrape_imdb_top_250()
    df.to_csv("imdb_top_250_updated.csv", index=False, encoding="utf-8")
    print(f"[SUCCESS] Extracted {len(df)} movies into 'imdb_top_250_updated.csv'")

"""
DuckDuckGo SERP Scraper - Extracts organic search results with ranking
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import csv
import time
import random

# Configuration
REQUEST_DELAY = (1, 3)  # Min/max seconds between requests
MAX_RETRIES = 2
CSV_FIELDS = ["search_term", "rank", "title", "url", "description"]

# Search terms to scrape
SEARCH_TERMS = [
    "ergonomic office chair",
    "polo t shirts for men",
    "bluetooth headphones",
    "coffee beans",
]


def setup_driver():
    """Configure Chrome WebDriver with anti-detection settings"""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Anti-bot detection settings
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)


def fetch_page(driver, search_term):
    """Get search results page with retry logic"""
    url = f"https://duckduckgo.com/?q={search_term.replace(' ', '+')}"
    
    for attempt in range(MAX_RETRIES):
        try:
            time.sleep(random.uniform(*REQUEST_DELAY))
            driver.get(url)
            
            # Wait for results to load
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "li[data-layout='organic']"))
            )
            return driver.page_source
        except Exception as e:
            if attempt == MAX_RETRIES - 1:
                print(f"Failed to fetch '{search_term}': {str(e)}")
            time.sleep(2**attempt)  # Exponential backoff
    return None


def parse_results(html, search_term):
    """Extract structured data from search results page"""
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")
    results = []
    
    # Process organic results
    organic_items = soup.select("li[data-layout='organic']")
    
    for rank, item in enumerate(organic_items, 1):
        try:
            result = item.select_one("article[data-nrn='result']")
            if not result:
                continue
                
            # Get title and URL
            title_elem = result.select_one("h2.LnpumSThxEWMIsDdAT17 a")
            url = title_elem.get("href") if title_elem else ""
            
            # Get description
            desc_elem = result.select_one("div[data-result='snippet']")
            
            results.append({
                "search_term": search_term,
                "rank": rank,
                "title": title_elem.get_text(strip=True) if title_elem else "",
                "url": url,
                "description": desc_elem.get_text(strip=True) if desc_elem else "",
            })
        except Exception as e:
            print(f"Error parsing result #{rank} for '{search_term}': {e}")
    
    return results


def main():
    """Run scraper and save results to CSV"""
    start_time = time.time()
    all_results = []

    try:
        driver = setup_driver()
        
        for term in SEARCH_TERMS:
            print(f"Scraping: '{term}'...")
            
            results = parse_results(fetch_page(driver, term), term)
            if results:
                all_results.extend(results)
                print(f"→ Captured {len(results)} results")
            
            # Delay between terms
            if term != SEARCH_TERMS[-1]:
                time.sleep(random.uniform(*REQUEST_DELAY))
    
    finally:
        # Ensure driver is closed
        if 'driver' in locals():
            driver.quit()
    
    # Write to CSV
    with open("duckduckgo-serp-results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(all_results)
    
    elapsed = time.time() - start_time
    print(f"\n✔ Success! Saved {len(all_results)} results in {elapsed:.2f} seconds")
    print(f"Results saved to 'duckduckgo-serp-results.csv'")


if __name__ == "__main__":
    main()
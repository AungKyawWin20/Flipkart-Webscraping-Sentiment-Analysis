from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor, as_completed
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import random
 
# Setup Options (Headless) 
def get_driver():
    options = Options()
    service = Service(ChromeDriverManager().install())
    options.add_argument('--headless=new')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    return webdriver.Chrome(service=service, options=options)

#  Class name mapping per search term 
CLASS_NAME_MAP = {
    "Samsung Phones": "CGtC98",
    "Macbooks": "CGtC98",
    "Remote Control Cars": "wjcEIp",
    "Engine Oil": "wjcEIp",
    "Antidepressants": "wjcEIp"
}

#  Get product links from a search term 
def get_product_links(search_term):
    driver = get_driver()
    driver.get("https://www.flipkart.com")

    try:
        close_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "_30XB9F"))
        )
        close_btn.click()
    except:
        pass

    try:
        searchbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "Pke_EE"))
        )
        searchbox.send_keys(search_term)
        searchbox.send_keys(Keys.RETURN)
    except Exception as e:
        print(f"Search failed: {e}")
        driver.quit()
        return []

    class_name = CLASS_NAME_MAP.get(search_term)
    links = []

    if class_name:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, class_name)))
            products = driver.find_elements(By.CLASS_NAME, class_name)
            for product in products:
                href = product.get_attribute("href")
                if href:
                    if not href.startswith("http"):
                        href = "https://www.flipkart.com" + href
                    links.append(href)
        except Exception as e:
            print(f"Could not extract links for {search_term} using class '{class_name}': {e}")
    else:
        print(f"No class name defined for: {search_term}")

    driver.quit()
    return links

#  Scrape product data from one product link 
def scrape_product(link):
    driver = get_driver()
    data = {}

    try:
        driver.get(link)
        wait = WebDriverWait(driver, 10)

        try:
            title = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "VU-ZEz"))).text
        except:
            title = None

        try:
            star_rating = driver.find_element(By.CLASS_NAME, "XQDdHH").text
        except:
            star_rating = None

        try:
            rating_info = driver.find_element(By.CLASS_NAME, "Wphh3N").text
            rating_count = rating_info.split()[0]
        except:
            rating_count = None

        try:
            breadcrumb = driver.find_elements(By.CLASS_NAME, "R0cyWM")
            category = breadcrumb[1].text
        except:
            category = None

        # Reviews link
        all_reviews = []

        # finding a review link more reliably
        try:
            reviews_link_element = driver.find_element(By.PARTIAL_LINK_TEXT, "All")
            reviews_url = reviews_link_element.get_attribute("href")
            print(f"Found reviews link for '{title}'")
        except Exception as e:
            print(f"Could not find reviews link for '{title}': {e}")
            reviews_url = None

        # If a reviews URL was found, loop through up to 10 review pages
        if reviews_url:
            for page in range(1, 11):
                try:
                    page_url = f"{reviews_url}&page={page}"
                    driver.get(page_url)
                    time.sleep(random.uniform(1.5, 2.5))  # Slightly random delay

                    # Basic CAPTCHA detection
                    if "captcha" in driver.page_source.lower():
                        print(f"CAPTCHA detected on page {page} for '{title}'. Stopping.")
                        break

                    review_elements = driver.find_elements(By.CLASS_NAME, "ZmyHeo")

                    if not review_elements:
                        print(f"No reviews found on page {page} for '{title}' — stopping.")
                        break

                    reviews = [r.text.strip() for r in review_elements if r.text.strip()]
                    print(f"Page {page}: Extracted {len(reviews)} reviews for '{title}'")
                    all_reviews.extend(reviews)

                except Exception as e:
                    print(f"Error scraping reviews on page {page} for '{title}': {e}")
                    break

        data = {
            'Title': title,
            'Star Rating': star_rating,
            'Rating Count': rating_count,
            'Category': category,
            'Reviews': " | ".join(all_reviews[:50]),
            'URL': link
        }

    except Exception as e:
        print(f"Error scraping {link}: {e}")
    finally:
        driver.quit()
        return data

#  Main Function: Run for multiple search terms 
def main(search_terms):
    all_data = []

    for term in search_terms:
        print(f"\n Searching for: {term}")
        product_links = get_product_links(term)
        print(f"Found {len(product_links)} product links for '{term}'")

        results = []

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(scrape_product, link) for link in product_links]
            for future in as_completed(futures):
                result = future.result()
                if result:
                    result["Search Term"] = term
                    results.append(result)

        all_data.extend(results)

    # Save all results
    df = pd.DataFrame(all_data)
    print(df)
    df.to_csv("flipkart_scraped_data.csv", index=False)

if __name__ == "__main__":
    search_terms = ["Samsung Phones", "Macbooks", "Remote Control Cars", "Engine Oil", "Antidepressants"]
    main(search_terms)

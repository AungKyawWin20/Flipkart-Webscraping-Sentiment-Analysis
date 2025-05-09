# 🛍️ Flipkart Product Scraper
A robust Python-based web scraper that extracts detailed product information from Flipkart, including reviews, ratings, and categories for NLP. Built with Selenium for reliable automation.

## ✨ Key Features

- **Multi-Category Scraping**: Scrapes data from multiple product categories
- **Parallel Processing**: Uses ThreadPoolExecutor for efficient scraping
- **Rich Data Extraction**:
    - Product titles and categories
    - Star ratings and review counts
    - Detailed user reviews (up to 50 per product)
    - Product URLs for reference
- **Anti-Detection Measures**: Implements headless browsing and automation detection bypass
- **Rate Limiting**: Random delays between requests to prevent blocking
- **CAPTCHA Detection**: Basic CAPTCHA detection to prevent invalid data collection
- **CSV Export**: Automatically exports data to CSV format

## 🚀 Getting Started

### Prerequisites

- **Python 3.7+**
- **Chrome** browser installed
- **Stable** internet connection

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/flipkart-scraper.git
cd flipkart-scraper
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

### Usage

Run the Script

```bash 
python Final_Code.py
```

The script will scrape data for:

- Samsung Phones  
- MacBooks  
- Remote Control Cars  
- Engine Oil  
- Antidepressants

## 📊 Output Format
The script generates a `flipkart_scraped_data.csv` file with the following columns:

- Title
- Star Rating
- Rating Count
- Category
- Reviews (up to 50 reviews per product)
- URL
- Search Term

## 🛠️ Technical Details

Built with:

- Selenium WebDriver for web automation
- webdriver_manager for ChromeDriver management
- pandas for data handling
- ThreadPoolExecutor for concurrent scraping

## ⚠️ Disclaimer

This tool is for educational purposes only. Please review Flipkart's terms of service and robots.txt before use. Be mindful of rate limiting and scraping policies.

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

# 🛍️ Flipkart Product Scraper and Sentiment Analyzer

A comprehensive Python project that combines web scraping and sentiment analysis to extract and analyze product information from Flipkart. Built with Selenium WebDriver for reliable automation and Transformers for sentiment analysis.

## ✨ Key Features

### Web Scraping

- **Multi-Category Scraping**: Scrapes data from multiple product categories simultaneously
- **Parallel Processing**: Uses ThreadPoolExecutor for efficient concurrent scraping (up to 10 workers)
- **Rich Data Extraction**:
  - Product titles and categories
  - Star ratings and review counts
  - Detailed user reviews (up to 50 per product)
  - Product URLs and search terms
  - Breadcrumb navigation data
- **Anti-Detection Measures**:
  - Headless browser operation
  - Automation detection bypass
  - Random delays between requests (1.5-2.5 seconds)
  - User-agent manipulation
  - Window size simulation
- **Error Handling**:
  - CAPTCHA detection and graceful handling
  - Connection error recovery
  - Missing element handling
- **Data Export**: Automatic CSV export with comprehensive product information

### Sentiment Analysis

- **Review Processing**: Analyzes customer reviews to determine sentiment
- **Deep Learning Model**: Uses state-of-the-art transformer models for accurate sentiment classification
- **Batch Processing**: Efficiently processes large volumes of reviews
- **Sentiment Metrics**: Provides detailed sentiment scores and analysis
- **Data Visualization**: Includes visualizations of sentiment distribution
- **Category-wise Analysis**: Breaks down sentiment by product categories

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Google Chrome browser
- Stable internet connection
- At least 4GB RAM recommended
- CUDA-compatible GPU (optional, for faster sentiment analysis)
- Windows/Linux/MacOS supported

### Installation

1. Clone the repository:

```bash
git clone https://github.com/AungKyawWin20/Flipkart-Webscraping-Sentiment-Analysis.git
cd Flipkart-Webscraping-Sentiment-Analysis
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

### Required Dependencies

- selenium==latest
- webdriver-manager==latest
- pandas==latest
- transformers==latest
- torch==latest
- numpy==latest

## 🔧 Usage

### Web Scraping

1. Run the scraping script:

```bash
python Final_Code.py
```

2. The script will automatically scrape data for these categories:

   - Samsung Phones
   - MacBooks
   - Remote Control Cars
   - Engine Oil
   - Antidepressants

3. Progress will be displayed in the console, showing:
   - Current search term being processed
   - Number of products found
   - Review collection progress
   - Any errors or CAPTCHA detections

### Sentiment Analysis

1. Run the Jupyter notebook:

```bash
jupyter notebook Flipkart_Sentiment_Analysis.ipynb
```

2. The notebook will:
   - Load the scraped data
   - Process and clean the reviews
   - Perform sentiment analysis
   - Generate visualizations and insights

## 📊 Output Files

### Scraped Data (flipkart_scraped_data.csv)

| Column       | Description                                   |
| ------------ | --------------------------------------------- |
| Title        | Product name                                  |
| Star Rating  | Product rating (0-5 stars)                    |
| Rating Count | Number of ratings received                    |
| Category     | Product category from breadcrumb              |
| Reviews      | Up to 50 reviews per product (pipe-separated) |
| URL          | Product page URL                              |
| Search Term  | Original search term used                     |

### Sentiment Analysis (flipkart_data_with_sentiment.csv)

- Original scraped data
- Sentiment scores
- Sentiment classifications
- Category-wise sentiment distribution

## 🛠️ Technical Implementation

### Web Scraping

- **Browser Automation**:

  - Selenium WebDriver with Chrome in headless mode
  - Automated ChromeDriver installation via webdriver_manager
  - Custom Chrome options for anti-bot measures

- **Concurrent Processing**:
  - ThreadPoolExecutor for parallel product scraping
  - Configurable worker pool (default: 10 workers)
  - Automatic thread management and cleanup

### Sentiment Analysis

- **Model**: Transformer-based sequence classification
- **Preprocessing**: Text cleaning and normalization
- **Batch Processing**: Efficient handling of large datasets
- **GPU Acceleration**: CUDA support for faster processing

## ⚠️ Rate Limiting & Ethics

- Random delays between requests (1.5-2.5 seconds)
- CAPTCHA detection and graceful termination
- Respects Flipkart's robots.txt
- Limited to 50 reviews per product
- Concurrent requests limited to 10

## 🔍 Troubleshooting

- **CAPTCHA Detection**: If encountered, the script will skip the current page and continue
- **Missing Elements**: Gracefully handled with None values
- **Network Issues**: Automatic retry mechanism for failed requests
- **Memory Usage**: Close browser instances after each scrape
- **Chrome Issues**: Ensure latest Chrome browser is installed
- **GPU Memory**: Adjust batch size for sentiment analysis if running out of memory

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## ⚖️ Disclaimer

This tool is for educational purposes only. Please review Flipkart's terms of service and robots.txt before use. Be mindful of rate limiting and scraping policies. Users are responsible for compliance with applicable laws and terms of service.

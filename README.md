# DuckDuckGo Search Scraper

[![Promo](https://github.com/luminati-io/LinkedIn-Scraper/blob/main/Proxies%20and%20scrapers%20GitHub%20bonus%20banner.png)](https://brightdata.com/products/serp-api/duckduckgo-search)

This repository offers two solutions for extracting data from DuckDuckGo Search Engine Results Pages (SERPs):

- **Free DuckDuckGo Scraper:** A tool for scraping DuckDuckGo Search Results at small scale
- **Enterprise-grade DuckDuckGo SERP API:** A scalable, production-ready solution for high-volume, real-time data extraction (part of [Bright Data's SERP Scraper API](https://brightdata.com/products/serp-api))

## Table of Contents

- [Free DuckDuckGo SERP Scraper](#free-duckduckgo-serp-scraper)
  - [Setup Requirements](#setup-requirements)
  - [Quick Start Guide](#quick-start-guide)
  - [Sample Output](#sample-output)
  - [Limitations](#limitations)
- [DuckDuckGo SERP API](#duckduckgo-serp-api)
  - [Key Benefits](#key-benefits)
  - [Getting Started](#getting-started)
- [Implementation Methods](#implementation-methods)
  - [Direct API Access](#direct-api-access)
  - [Native Proxy-Based Access](#native-proxy-based-access)
- [DuckDuckGo Search Query Parameters](#duckduckgo-search-query-parameters)
  - [Localization](#localization)
  - [Safe Search Configuration)](#safe-search-configuration-kp)
  - [Time Range Filtering](#time-range-filtering-df)
  - [Device Targeting](#device-targeting-brd_mobile)
  - [Browser Emulation](#browser-emulation-brd_browser)
- [Practical Example](#practical-example)
- [Support & Resources](#support--resources)

## Free DuckDuckGo SERP Scraper
The Free DuckDuckGo SERP Scraper offers a straightforward method for collecting search result data on a smaller scale. It’s perfect if you need limited data without the overhead of managing proxies or handling high volumes.

<img width="800" alt="free-duckduckgo-serp-scraper" src="https://github.com/user-attachments/assets/0472593e-615c-4723-96e7-08f83cb0b477" />

### Setup Requirements

- **Python 3.9+** – [Download Python](https://www.python.org/downloads/)
- **Required Packages:**
    - `selenium` (for browser automation)
    - `webdriver-manager` (for managing browser drivers)
    - `beautifulsoup4` (for HTML parsing)

Install the packages using:
```bash
pip install selenium webdriver-manager beautifulsoup4
```

> **New to Web Scraping?** <br>
Kickstart your journey with our [Beginner’s Guide to Web Scraping with Python](https://brightdata.com/blog/how-tos/web-scraping-with-python). Then, level up with our [Using Selenium for Web Scraping](https://brightdata.com/blog/how-tos/using-selenium-for-web-scraping) tutorial, and if you’re already comfortable with Selenium, take your skills further with our advanced [SeleniumBase guide](https://brightdata.com/blog/web-data/web-scraping-with-seleniumbase).
>

### Quick Start Guide

1. Open the [duckduckgo-serp-scraper.py](https://github.com/triposat/DuckDuckGo-Search-Scraper/blob/main/duckduckgo-serp-scraper/duckduckgo-serp-scraper.py) file.
2. Customize the search terms as needed:
    
    ```python
    SEARCH_TERMS = [
        "ergonomic office chair",
        "coffee maker",
    ]
    ```
    
3. Run the script to begin scraping.

### Sample Output
Below is a preview of the scraper output:

<img width="800" alt="free-duckduckgo-serp-scraper-output" src="https://github.com/user-attachments/assets/d6891a93-2b5f-4243-8a17-e2a037c91570" />


### Limitations

Keep in mind that while the free scraper is great for basic tasks, it has some important limitations:

- High risk of IP blocking with frequent use
- Limited request volume capacity
- Frequent CAPTCHA interruptions
- Not suitable for production environments

For a scalable and stable solution, consider Bright Data's dedicated API detailed below 👇

## DuckDuckGo SERP API

The DuckDuckGo SERP API is part of Bright Data’s comprehensive [SERP Scraper API](https://brightdata.com/products/serp-api) suite. It leverages our industry-leading [DuckDuckGo proxy infrastructure](https://brightdata.com/solutions/duckduckgo-proxies) to deliver real-time DuckDuckGo search results with a single API call.

### Key Benefits

- **Global Accuracy**: Get tailored results for specific locations worldwide.
- **Pay-Per-Success**: You pay only for successful requests.
- **Real-Time Data**: Access up-to-date search results in seconds.
- **Unlimited Scalability**: Handle high-volume scraping effortlessly.
- **Cost-Efficient**: No need for expensive infrastructure.
- **Reliable Performance**: Advanced anti-blocking technology ensures consistent results.
- **24/7 Expert Support**: Get assistance whenever you need it.

📌 Try Before You Buy: Experience our solution with the [SERP API Live Demo](https://brightdata.com/products/serp-api/duckduckgo-search).

<img width="800" alt="bright-data-serp-api-playground" src="https://github.com/user-attachments/assets/fc60e165-e4db-41d2-93eb-2b6a01398353" />

### Getting Started

1. [Create a Bright Data account](https://brightdata.com/) (new users receive a $5 credit).
2. Generate your [API key](https://docs.brightdata.com/general/account/api-token).
3. Follow our [step-by-step configuration guide](https://github.com/triposat/DuckDuckGo-Search-Scraper/blob/main/setup-serp-api.md) to integrate the SERP API.

## Implementation Methods

You can integrate the DuckDuckGo SERP API into your workflow using one of two approaches:

### Direct API Access

Make a direct request to Bright Data’s API endpoint.

#### cURL Example

```bash
curl https://api.brightdata.com/request \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer API_TOKEN" \
  -d '{
        "zone": "ZONE_NAME",
        "url": "https://duckduckgo.com/?q=budget+laptops+under+500+gbp&kl=uk-en&kad=en-gb&df=w",
        "format": "raw"
      }'
```

#### Python Example

```python
import requests

url = "https://api.brightdata.com/request"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer API_TOKEN"
}

payload = {
    "zone": "ZONE_NAME",
    "url": "https://duckduckgo.com/?q=budget+laptops+under+500+gbp&kl=uk-en&kad=en-gb&df=w",
    "format": "raw",
}

response = requests.post(url, headers=headers, json=payload)

with open("duckduckgo-scraper-api-result.html", "w", encoding="utf-8") as file:
    file.write(response.text)

print("Response saved!")
```

### Native Proxy-Based Access

Use proxy routing for direct access to search results.

#### cURL Example

```bash
curl -i \
  --proxy brd.superproxy.io:33335 \
  --proxy-user brd-customer-<CUSTOMER_ID>-zone-<ZONE_NAME>:<ZONE_PASSWORD> \
  -k \
  "https://duckduckgo.com/?q=budget+laptops+under+500+gbp&kl=uk-en&kad=en-gb&df=w"
```

#### Python Example

```python
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = "brd.superproxy.io"
port = 33335
username = "brd-customer-<CUSTOMER_ID>-zone-<ZONE_NAME>"
password = "<ZONE_PASSWORD>"
proxy_url = f"http://{username}:{password}@{host}:{port}"

proxies = {
    "http": proxy_url,
    "https": proxy_url
}

url = "https://duckduckgo.com/?q=budget+laptops+under+500+gbp&kl=uk-en&kad=en-gb&df=w"
response = requests.get(url, proxies=proxies, verify=False)

with open("duckduckgo-scraper-api-result.html", "w", encoding="utf-8") as file:
    file.write(response.text)

print("Response saved!")
```

> Note: For production use with the native proxy approach, installing Bright Data’s SSL certificate is recommended. Refer to our [SSL Certificate Guide](https://docs.brightdata.com/general/account/ssl-certificate) for details.
> 

👉 For a full preview of the HTML output, see the [complete result](https://github.com/triposat/DuckDuckGo-Search-Scraper/blob/main/duckduckgo-scraper-api-output/duckduckgo-scraper-api-result.html).


## DuckDuckGo Search Query Parameters

Fine-tune your search results by using various query parameters.

### Localization

#### Country and Language (`kl`)

Specifies the country and language for search results.

*Example:*

```bash
curl --proxy brd.superproxy.io:33335 \
     --proxy-user brd-customer-<id>-zone-<zone>:<password> \
     "https://duckduckgo.com/?q=best+coffee+brands&kl=it-it"
```

This returns search results tailored for Italy.

#### Interface Language (`kad`)

Controls the language of the DuckDuckGo interface.

*Example:*

```bash
https://duckduckgo.com/?q=photo+editing+tools&kad=de
```

This keeps the search content in English while displaying the interface in German.

### Safe Search Configuration (`kp`)

Adjusts content filtering for adult material.

#### Values

- `1` – Strict Safe Search
- `-1` – Moderate
- `-2` – Off

*Example:*

```bash
https://duckduckgo.com/?q=swimsuit&kp=1
```

Returns only family-safe results for *"swimsuit”.*

### Time Range Filtering (`df`)

Limits search results to a specific time frame.

#### Values

- `d` – Past day
- `w` – Past week
- `m` – Past month
- `y` – Past year
- *Custom range:* e.g., `2025-03-01..2025-03-10`

*Example:*

```bash
https://duckduckgo.com/?q=iphone+15+review&df=w
```

Shows only recent reviews (within the last week).

### Device Targeting (`brd_mobile`)

Simulate searches from various device types.

#### Options

- `0` – Desktop (default)
- `1` – Random mobile device
- `ios` or `iphone` – iPhone
- `ipad` or `ios_tablet` – iPad
- `android` – Android phone
- `android_tablet` – Android tablet

 *Example:*

```bash
https://duckduckgo.com/?q=top+travel+apps&brd_mobile=ios
```

This simulates an iPhone user. You might see app store links, mobile-focused content, or AMP pages.

### Browser Emulation (`brd_browser`)

Specify the browser’s user-agent for the request.

#### Options

- Default (random browser)
- `chrome` – Google Chrome
- `safari` – Safari
- `firefox` – Mozilla Firefox *(not compatible with `brd_mobile=1`)*

*Example:*

```bash
https://duckduckgo.com/?q=best+vpn+services&brd_browser=safari
```
This simulates a Safari browser, providing insights into how content is displayed and ranked on that platform.

## Practical Example

You're monitoring competitors' pricing pages for *"budget laptops under £500"* in the UK, targeting mobile users.

Your goal is to:

- Simulate a UK-based mobile user
- Get localized English results (UK-specific retailers, currency)
- Use a mobile Chrome user agent (to capture mobile-specific results like AMP pages)
- Focus on recent product listicles or deals

Combine these requirements in a single cURL command:

```bash
curl --proxy brd.superproxy.io:33335 \
     --proxy-user brd-customer-<CUSTOMER_ID>-zone-<ZONE_NAME>:<ZONE_PASSWORD> \
     "https://duckduckgo.com/?\
q=budget+laptops+under+500+gbp&\
kl=uk-en&\
kad=en-gb&\
df=w&\
brd_mobile=android&\
brd_browser=chrome"
```
🎯 This fetches **mobile-first**, **localized**, and **recent** content.

## Support & Resources

- **Documentation:** [SERP API Documentation](https://docs.brightdata.com/scraping-automation/serp-api/)
- **Related APIs:**
    - [SERP API](https://github.com/luminati-io/serp-api)
    - [Google Search API](https://github.com/luminati-io/google-search-api)
    - [Google News Scraper](https://github.com/luminati-io/Google-News-Scraper)
    - [Google Trends API](https://github.com/luminati-io/google-trends-api)
    - [Google Reviews API](https://github.com/luminati-io/google-reviews-api)
    - [Google Hotels API](https://github.com/luminati-io/google-hotels-api)
    - [Google Flights API](https://github.com/luminati-io/google-flights-api)
    - [Web Unlocker API](https://github.com/luminati-io/web-unlocker-api)
- **Use Cases:**
    - [SEO & SERP Tracking](https://brightdata.com/use-cases/serp-tracking)
    - [Travel Industry Data](https://brightdata.com/use-cases/travel)
- **Additional Reading:** [Best SERP APIs](https://brightdata.com/blog/web-data/best-serp-apis)
- **Contact Support:** [support@brightdata.com](mailto:support@brightdata.com)

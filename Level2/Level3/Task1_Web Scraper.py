import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://quotes.toscrape.com/"

try:
    # Send HTTP request
    response = requests.get(url, timeout=10)

    # Show status code (helps debugging)
    print("Status Code:", response.status_code)

    # Raise error for 4xx / 5xx
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    print("\nQuotes from the website:\n")

    # Extract quotes
    quotes = soup.find_all("span", class_="text")

    for i, quote in enumerate(quotes, start=1):
        print(f"{i}. {quote.text}")

except requests.exceptions.HTTPError:
    print("❌ HTTP error occurred (page not accessible)")
except requests.exceptions.ConnectionError:
    print("❌ Connection error (check your internet)")
except requests.exceptions.Timeout:
    print("❌ Request timed out")
except Exception as e:
    print("❌ Error:", e)


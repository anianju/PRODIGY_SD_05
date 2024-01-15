import csv
import requests
from bs4 import BeautifulSoup

def scrape_and_save_product_info(url, output_file):
   
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

       
        product_names = [name.text.strip() for name in soup.select('.product-name')]
        product_prices = [price.text.strip() for price in soup.select('.product-price')]
        product_ratings = [rating.text.strip() for rating in soup.select('.product-rating')]

        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Product Name', 'Price', 'Rating']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for name, price, rating in zip(product_names, product_prices, product_ratings):
                writer.writerow({'Product Name': name, 'Price': price, 'Rating': rating})

        print(f"Product information has been scraped and saved to {output_file}")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

if __name__ == "__main__":
    website_url = 'https://www.flipkart.in'
    output_csv_file = 'product_information.csv'

    scrape_and_save_product_info(website_url, output_csv_file)


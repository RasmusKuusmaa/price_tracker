import requests
from bs4 import BeautifulSoup

def get_price(url):
    headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/112.0.0.0 Safari/537.36"
        )
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        price = soup.find('span', class_='price__original')
        if price:
            return price.get_text()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request exception: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    product_url = "https://www.euronics.ee/it/tahvelarvutid/graafikalauad/ctl-6100wlk-n/wacom-intuos-m-bluetooth-must-graafikalaud"
    price = get_price(product_url)
    if price:
        print(f"hind: {price}")
    else:
        print('failed')
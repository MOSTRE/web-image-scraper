import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to download an image from a URL
def download_image(url, directory):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_name = os.path.basename(url)
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'wb') as f:
                f.write(response.content)
                print(f'{file_name} downloaded successfully.')
        else:
            print(f'Failed to download {url}: {response.status_code}')
    except Exception as e:
        print(f'Error downloading {url}: {e}')

# Function to scrape images from a webpage
def scrape_images(url, output_directory):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            images = soup.find_all('img')
            for img in images:
                img_url = img.get('src')
                if img_url:
                    img_url = urllib.parse.urljoin(url, img_url)
                    download_image(img_url, output_directory)
        else:
            print(f'Failed to fetch webpage: {response.status_code}')
    except Exception as e:
        print(f'Error scraping images: {e}')

def main():
    website_url = input("Enter the URL of the website: ")
    output_directory = input("Enter the directory to save images: ")

    create_directory(output_directory)
    scrape_images(website_url, output_directory)

if __name__ == "__main__":
    main()

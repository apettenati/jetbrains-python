import os
import requests
from bs4 import BeautifulSoup
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

def get_url():
    url = input()
    if url == 'exit':
        sys.exit()
    else:
        url = f'http://{url}'
    return url

def check_HTTP_status(request):
    if request.status_code == 200:
        return True
    else:
        print("Something is wrong with your internet connection")
        return False

def create_request(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}
    request = requests.get(url, headers=headers)
    return request

def create_soup(request):
        soup = BeautifulSoup(request.content, 'html.parser')
        return soup

def valid_url(url):
    valid_urls = [ "http://bloomberg.com", "http://nytimes.com"]
    if "." in url:
        if url in valid_urls:
            return True
        else:
            print("Error: Invalid URL")
            return False
    else:
        print("Error: Invalid URL")
        return False

def read_url(url, soup):
    output = soup.find('body').text
    return output

def read_CLI():
    args = sys.argv
    directory = args[1]
    return directory

def make_dir(directory):
    try:
        if not os.path.exists("directory"):
            os.mkdir(f"C:\\Users\\Amanda\\Google Drive\\python\\Text-Based Browser\\Text-Based Browser\\task\\{directory}")
    except FileExistsError:
        pass

def write_file(url, directory, output):
    url = url.strip(".com").strip("http://")
    filename = f"C:\\Users\\Amanda\\Google Drive\\python\\Text-Based Browser\\Text-Based Browser\\task\\{directory}\\{url}"
    with open(filename, "a") as f:
        f.write(output)


def main():
    directory = read_CLI()
    # directory = "testtest"
    make_dir(directory)
    while True:
        url = get_url()
        if valid_url(url):
            request = create_request(url)
            if check_HTTP_status(request):
                soup = create_soup(request)
                output = read_url(url, soup)
                print(output)
                write_file(url, directory, output)

if __name__ == "__main__":
    main()

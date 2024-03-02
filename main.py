import requests
from bs4 import BeautifulSoup
import re

# Function to extract text from a webpage
def extract_text(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract text
        text = soup.get_text()
        return text
    except Exception as e:
        print(f"Error occurred while extracting text from {url}: {e}")
        return ""

# Function to get all links from a webpage and ignore image links
def get_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all anchor tags
        links = soup.find_all('a', href=True)
        # Extract href attribute from anchor tags, filtering out image links
        hrefs = [link['href'] for link in links if not re.match(r'.*\.(png|jpg)$', link['href'])]
        return hrefs
    except Exception as e:
        print(f"Error occurred while getting links from {url}: {e}")
        return []

# Function to recursively crawl and extract text from all pages
def crawl(url, visited, max_depth, current_depth=0):
    if url in visited or current_depth >= max_depth:
        return

    visited.add(url)
    print(f"Crawling: {url}")

    text = extract_text(url)
    if text:
        with open("scraped_data.txt", "a", encoding="utf-8") as f:
            f.write(text)
            f.write("\n\n")

    links = get_links(url)
    for link in links:
        if link.startswith("http") and "merrimackvalleyroofing.com" in link:
            crawl(link, visited, max_depth, current_depth + 1)

def remove_newlines(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Remove newline characters
        content = content.replace("\n", "")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print("Newline characters removed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    start_url = "https://www.merrimackvalleyroofing.com/"
    max_depth = 3  # Maximum depth to crawl
    visited = set()
    crawl(start_url, visited, max_depth)

# Path to the file
file_path = "scraped_data.txt"

# Call the function to remove newlines
if __name__ == "__main__":
    main()
    remove_newlines(file_path)
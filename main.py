import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://www.merrimackvalleyroofing.com"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Now you can perform scraping operations using BeautifulSoup
    # For example, let's print the title of the webpage
    print("Title of the webpage:", soup.title.text)
    
    # You can find specific elements using their tags, classes, ids, etc.
    # For example, let's find all the <a> tags with class="nav-link" (navigation links)
    nav_links = soup.find_all("a", class_="nav-link")
    
    # Print out the text content of each navigation link
    print("\nNavigation Links:")
    for link in nav_links:
        print(link.text.strip())  # .strip() removes leading/trailing whitespaces
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

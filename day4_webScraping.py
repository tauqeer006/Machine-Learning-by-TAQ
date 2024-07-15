from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.motorola.com/us/home-and-office-phones"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "lxml")

# List for main headings
lists = [h1.text.strip() for h1 in soup.find_all("h1")]

# List for contact details
list1 = [p.text.strip() for p in soup.find_all("p", class_="subhead")]

# List for website facilities
list2 = [div.text.strip() for div in soup.find("div", class_="container")]  # Example, adjust as per actual structure

# List for about section
list3 = [footer.text.strip() for footer in soup.find_all("footer", class_="checkout-footer")]

# List for footer details
list4 = [section.text.strip() for section in soup.find_all("section", class_="checkout-footer-copy")]

# Print lengths of lists to debug
print(f"Length of lists: {len(lists)}")
print(f"Length of contact details: {len(list1)}")
print(f"Length of website facilities: {len(list2)}")
print(f"Length of about section: {len(list3)}")
print(f"Length of footer details: {len(list4)}")

# Ensure all lists have the same length
min_length = min(len(lists), len(list1), len(list2), len(list3), len(list4))
lists = lists[:min_length]
list1 = list1[:min_length]
list2 = list2[:min_length]
list3 = list3[:min_length]
list4 = list4[:min_length]

# Create dictionary
dicts = {"Main headings": lists,
         "contact details": list1,
         "Website Facilities": list2,
         "About Website": list3,
         "Footer Website": list4}

# Create DataFrame
data = pd.DataFrame(dicts)
print(data)

import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://webscraper.io/test-sites/e-commerce/allinone/{}"

query = "computers/tablets"
res = requests.get(baseurl.format(query))
soup = BeautifulSoup(res.text, 'html.parser')

data = []  # Initialize an empty list to store the extracted data

products = soup.find_all('div', class_='product-wrapper')
for i in products:
    price = i.find('h4', class_='price').text
    name = i.find('a', class_='title').text
    des = i.find('p', class_='description').text
    review = i.find('div', class_='ratings').findAll('p')
    reviews = review[0].text
    ratings = review[1]['data-rating']
    
    # Append the extracted data as a dictionary to the list
    data.append({'Price': price, 'Name': name, 'Description': des, 'Reviews': reviews, 'Ratings': ratings})

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('products.csv', index=False)

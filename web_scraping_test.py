"""import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks'

response = requests.get(url)
html_data = response.text
print(html_data[961:984]) # List of largest banks -


# Define the URL of the webpage
url = 'YOUR_URL'

# Send an HTTP GET request to the URL and retrieve the page content
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table with the data you want (you may need to inspect the webpage's HTML to find the correct table)
table = soup.find('table', {'id': 'table_id'})  # Replace 'table_id' with the actual ID of the table

# Initialize lists to store the data
bank_names = []
market_caps = []

# Iterate through the table rows and extract the data
for row in table.find_all('tr')[1:]:  # Skip the header row
    columns = row.find_all('td')
    bank_name = columns[1].text.strip()  # Assuming the bank name is in the second column
    market_cap = columns[2].text.strip()  # Assuming the market cap is in the third column
    bank_names.append(bank_name)
    market_caps.append(market_cap)

# Create a Pandas DataFrame
data = {'Bank Name': bank_names, 'Market Cap (US$ Billion)': market_caps}
df = pd.DataFrame(data)

# Display the first five rows using head
print(df.head())
"""

import requests
import pandas as pd
import json

# Write your code here
url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=e5912b969a34e36999062fc0ee43f3bc"  #Make sure to change ******* to your API key.
response = requests.get(url)
api_response_text = response.text
#print(api_response_text)
data = json.loads(api_response_text)

rates = data["rates"]

# Create a DataFrame from the rates dictionary
df = pd.DataFrame(rates.items(), columns=['Currency', 'Rate'])

# Set the 'Currency' column as the index
df.set_index('Currency', inplace=True)

# Display the DataFrame
print(df)
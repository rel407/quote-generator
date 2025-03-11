import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs
import sqlite3

# URL
url = "https://www.shopify.com/blog/motivational-quotes"

# GET content from desired webpage (URL)
response = rq.get(url)

# Test page accessability
if response.status_code == 200:
    print("Success")
else:
    print(f'Failed to retrieve page. Status code: {response.status_code}')

# Parse the HTML Data
soup = bs(response.text, 'html.parser')

# Find Quote Containers
target_li = soup.find_all('li', string=lambda text: text and '"' and '—' in text)

# Declare total number of items there are -- will use at the end to show how many of total items were added
total_items = len(target_li)

# Create empty list for the Quotes and Authors
quotes = []
authors = []

# Loop through the target list item elements
for li in target_li:
    # Strip li items of any extra spaces and get rid of element tags
    text = li.get_text(strip=True)
    
    if "—" in text:
        
        # Split the Quote and Author from one another
        quot, auth = text.rsplit("—", 1)
        
        # Clean Up the quote and author items
        cleaned_quote = quot.strip().strip("“”")
        cleaned_author = auth.strip()
        
        # Add the cleaned up quote and author to their corresponding lists
        quotes.append(cleaned_quote)
        authors.append(cleaned_author)

# Print the results
print(len(quotes),"/",total_items, " quotes have been added.")
print(len(authors),"/",total_items, " authors have been added.")

'''
# Export to Excel
df1 = pd.DataFrame(quotes, columns=["quote"])
df2 = pd.DataFrame(authors, columns=["author"])

with pd.ExcelWriter('quotes.xlsx', engine='openpyxl') as writer:
    df1.to_excel(writer, sheet_name='quotes', index=False)
    df2.to_excel(writer, sheet_name='authors', index=False)
    
print("quotes.xlsx has created successfully")
'''

# Connect to SQLite database (or create it)
conn = sqlite3.connect('quotes-proj.db')
c = conn.cursor()

# Create authors table
c.execute('''CREATE TABLE IF NOT EXISTS authors (author_id INTEGER PRIMARY KEY, author VARCHAR(50) UNIQUE)''')
print("The 'authors' table has been created.")

# Create quotes table
c.execute('''CREATE TABLE IF NOT EXISTS quotes (quote_id INTEGER PRIMARY KEY, quote TEXT, author_id INTEGER, FOREIGN KEY (author_id) REFERENCES authors(author_id))''')
print("The 'quotes' table has been created.")


# Insert unique authors into the 'authors' table
author_ids = {}

for author in authors:
    
    #Check if the author is already in the database
    c.execute('SELECT author_id FROM authors WHERE author = ?', (author,))
    result = c.fetchone()
    
    if result:
        author_id = result[0]
    else:
        c.execute('INSERT INTO authors(author) VALUES (?)', (author,))
        author_id = c.lastrowid
        
    # Store the author_id for later use in the quotes table
    author_ids[author] = author_id
    
# Insert quotes into the 'quotes' table
for quote, author in zip(quotes, authors):
    author_id = author_ids[author]
    c.execute('''
        INSERT INTO quotes(quote, author_id)
        VALUES(?, ?)
        
                   ''', (quote, author_id))

#conn.commit()
conn.close()

print('Data inserted successfully')
''' beautifulsoup extract the data from the html  
it Finds tags, classes, ids , Navigates HTML easily but  Cannot fetch website itself
🔹 Use when: Extracting data from HTML , Parsing scraped pages
'''
# bs4 and requests is good for basic scraping
# bs4 and selenium is best for dynamic scraping
import requests
from bs4 import BeautifulSoup
import time
# we could use find and find all
# 1. Setup (URL + Headers)
url = "https://quotes.toscrape.com"
# header contain the information for the website to tell about you
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive"
}
'''
Types of Parsers in BeautifulSoup

Parser        | Speed       | Accuracy    | Install Needed | Use Case        | Behaviour
--------------|-------------|-------------|----------------|-----------------|------------------------------
html.parser   | Slow        | Medium      | No             | Simple tasks    | May produce incorrect structure
lxml          | Fast        | High        | Yes            | Best overall    | Fixes most issues
html5lib      | Very slow   | Very High   | Yes            | Broken HTML     | Mimics browser exactly
xml           | Fast        | Strict      | Yes (lxml)     | XML parsing     | Strict structure parsing
'''
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml") #used lxml praser 
# 2. Basic Info (title give the tag with text but .text gives just the text without the tag )
print("TITLE:", soup.title.text)
# 3. Find Single Element
first_quote = soup.find("span", class_="text")
if first_quote:
    print("\nFirst Quote:", first_quote.text)
# 4. Find Multiple Elements
quotes = soup.find_all("span", class_="text")
print("\nAll Quotes:")
for q in quotes:
    print("-", q.text)
# 5. Extract Links
print("\nLinks:")
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        print(href)
# 6. CSS Selectors
print("\nUsing CSS Selectors:")
for item in soup.select("div.quote span.text"):
    print(item.text)
# 7. Get Attributes
tag = soup.find("a")
if tag:
    print("\nExample Attribute (href):", tag.get("href"))
# 8. Clean Text (.strip() removes leading spaces and trailing spaces )
clean_text = soup.get_text().strip()
print("\nCleaned Text (first 200 chars):")
print(clean_text[:200])
# 9. Traverse DOM
div = soup.find("div", class_="quote")
if div:
    print("\nParent:", div.parent.name)
    print("Children:")
    for child in div.children:
        print(child)
# 10. Modify HTML
tag = soup.find("h1")
if tag:
    tag.string = "Modified Title"
print("\nModified HTML Title:")
print(soup.title.text)
# 11. Extract Images (if any)
print("\nImages:")
images = soup.find_all("img")
for img in images:
    print(img.get("src"))
# 12. Pretty Print
print("\nPretty HTML (short preview):")
print(soup.prettify()[:500])
# 13. Handle Tables (if present)
table = soup.find("table")
if table:
    print("\nTable Data:")
    for row in table.find_all("tr"):
        cols = row.find_all("td")
        data = [col.text.strip() for col in cols]
        print(data)
else:
    print("\nNo table found on this page.")
# 14. Delay (Anti-blocking)
time.sleep(2)
print("\n✅ Scraping Completed Successfully!")
# display the html file in pretty format 
print(soup.prettify())
# gives me the class of the p tag
soup.p['class']
# .string returns the only the direct text inside the tag but .text / .get_text() reutrn all the text inside the tag 
# returns the parent  
soup.p.parent
# return the name of parent 
print(soup.p.parent.name)
# return the child (.children reutrn the direct child but the .discendent return the all nested child )
soup.p.children
# return the name of the children
for child in soup.p.children:
    if child.name:   # ignore text nodes
        print(child.name)
# returns the name of title 
soup.title.name
# .attrs Gets all attributes of a tag (dictionary)
tag = soup.a
print(tag.attrs)
# if i want to get specific attribute then 
tag['href']        
tag.get('class')   


tag.parent
tag.children
tag.descendants
tag.next_sibling
tag.previous_sibling
soup.find('p')                  # first <p>
soup.find_all('p')              # all <p>
soup.find(id="main")            # by id
soup.find(class_="text")        # by class
soup.select('div p')            # p inside div
soup.select('.class')           # class
soup.select('#id')              # id
tag.parent
tag.children
tag.descendants
tag.next_sibling
tag.previous_sibling
tag.decompose()     # delete
tag.extract()       # remove and keep
tag.clear()         # remove content
# open the local ifle for scraping 
with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser') # use html.praser 
# gives all children of html in list form 
list(soup.children)
# gives the number of children 
len(list(soup.children))
# give the raw data 
st = "hello\nworld"
repr(st) # gives "hello\nworld"
# .next_sibling → next thing beside it 
soup.b.next_sibling
# .previous_sibling → previous thing beside it 
soup.b.previous_sibling
# .next_element → next item in full parse order
soup.b.next_element
# .previous_element → previous item in full parse order
soup.c.previous_element
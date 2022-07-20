#Use request library to download web pages
!pip install requests --quiet
import requests
topics_url = 'https://github.com/topics'
response = requests.get('https://github.com/topics')
response.status_code
len(response.text)
page_contents = response.text
page_contents
with open('webpage.html', 'w') as f:
    f.write(page_contents)
    
#Use BeautifulSoup to parse and extract information
!pip install beautifulsoup4
from bs4 import BeautifulSoup
doc = BeautifulSoup(page_contents, 'html.parser')
type(doc)
topic_title_tags = doc.find_all('p', class_ = 'f3 lh-condensed mb-0 mt-1 Link--primary')
topic_desc_tags = doc.find_all('p', class_ = 'f5 color-fg-muted mb-0 mt-1')
len(topic_desc_tags)
topic_desc_tags[:5]
repo_url = doc.find_all('a', class_ = 'no-underline flex-1 d-flex flex-column')
topic_url0 ="https://github.com" + repo_url[0]['href']
topic_url0
topic_titles = [ ]

for tag in topic_title_tags :
    topic_titles.append(tag.text)
    
print(topic_titles)

topic_desc = [ ]

for tag in topic_desc_tags :
    topic_desc.append(tag.text.strip())
    
print(topic_desc)

topic_urls = []
base = 'https://github.com'

for tags in repo_url:
    topic_urls.append(base + tags['href'])
    
print(topic_urls)

topic_dict = {
    'title' : topic_titles,
    'description' : topic_desc,
    'url' : topic_urls
}

topic_dict

topics_df = pd.DataFrame(topic_dict, index = None)

topics_df

#Create csv file with extracted information
topics_df .to_csv('topics.csv', index = None)

#Getting information out a topic page
topic_page_url = topic_urls[0]
reponse = requests.get(topic_page_url)
reponse.status_code
len(response.text)
topic_doc = BeautifulSoup(reponse.text, 'html.parser')
repo_tags = topic_doc.find_all('h3', class_='f3 color-fg-muted text-normal lh-condensed')
len(repo_tags)
a_tags[0].text.strip()
repo_url= base + a_tags[1]['href']
repo_url
star_tags= topic_doc.find_all('span', class_ = 'd-inline')
len(star_tags)
stars = topic_doc.find_all('span', class_ = 'Counter js-social-count')
stars[0].text.strip()

def num(star_text):
    star_text = star_text.strip()
    if ''

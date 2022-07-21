#!/usr/bin/env python
# coding: utf-8

# # TOP REPOSITORIES ON GITHUB TOPICS
# 

# ## Pick a website and describe your objective
# 

# -Pick website to scrap.Check project ideas section for inspiration.
# 
# -Decide which information your are going to scrap.Decide which format of csv output to use.
# 
# -Summary your project idea and and outline strategy in jupyter.
# 
# 

# ## Project Outline
# 

# 1.We are going to scrap https://github.com/topics.
# 
# 2.we will get a list of topics.For each topic will get topic title, topic page url and topic description.
# 
# 3.For each topic we will get 25 repositories in the topic from the topic page.
# 
# 4.For each repository we will grab repo name, username, stars and repo url.
# 
# 5.For each topic we will create a CSV file in the format
# 
# '''
# Repo Name,Username,Stars,Repo URL
# '''
# 

# ### Use request library to download web pages

# In[ ]:


get_ipython().system('pip install requests --quiet')


# In[ ]:


import requests


# In[ ]:


topics_url = 'https://github.com/topics'


# In[ ]:


response = requests.get('https://github.com/topics')


# In[ ]:


response.status_code


# In[ ]:


len(response.text)


# In[ ]:


page_contents = response.text


# ### Use BeautifulSoup to parse and extract information

# In[ ]:


get_ipython().system('pip install beautifulsoup4')


# In[ ]:


from bs4 import BeautifulSoup
doc = BeautifulSoup(page_contents, 'html.parser')
type(doc)


# In[ ]:


topic_title_tags = doc.find_all('p', class_ = 'f3 lh-condensed mb-0 mt-1 Link--primary')
topic_desc_tags = doc.find_all('p', class_ = 'f5 color-fg-muted mb-0 mt-1')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


len(topic_title_tags)


# In[ ]:


len(topic_desc_tags)


# In[ ]:


topic_desc_tags[:5]


# In[ ]:


repo_url = doc.find_all('a', class_ = 'no-underline flex-1 d-flex flex-column')
topic_url0 ="https://github.com" + repo_url[0]['href']
topic_url0


# In[ ]:


topic_titles = [ ]

for tag in topic_title_tags :
    topic_titles.append(tag.text)
    
print(topic_titles)


# In[ ]:


topic_desc = [ ]

for tag in topic_desc_tags :
    topic_desc.append(tag.text.strip())
    
print(topic_desc)


# In[ ]:


topic_urls = []
base = 'https://github.com'

for tags in repo_url:
    topic_urls.append(base + tags['href'])
    
print(topic_urls)


# In[ ]:


get_ipython().system('pip install pandas --quiet')

import pandas as pd



# In[ ]:


topic_dict = {
    'title' : topic_titles,
    'description' : topic_desc,
    'url' : topic_urls
}


# In[ ]:


import pandas as pd


# In[ ]:


topics_df = pd.DataFrame(topic_dict, index = None)


# ### Create csv file with extracted information

# In[ ]:


topics_df .to_csv('topics.csv', index = None)


# ### Getting information out a topic page

# In[104]:


topic_page_url = topic_urls[0]
reponse = requests.get(topic_page_url)
topic_doc = BeautifulSoup(reponse.text, 'html.parser')
repo_tags = topic_doc.find_all('h3', class_='f3 color-fg-muted text-normal lh-condensed')
a_tags = repo_tags[0].find_all('a')
username = a_tags[0].text.strip()
repo_name = a_tags[1].text.strip()
repo_url= base + a_tags[1]['href']
stars = topic_doc.find_all('span', class_ = 'Counter js-social-count')
stars_str = stars[0].text.strip()

def num_star_count(star_text):
    star_text = star_text.strip()
    if stars_str[-1] == 'k' :
        return int(float (stars_str[:-1]) * 1000)
    return int(stars_str)




def get_repo_info(h3_tag, star_tag):
    #returns all required info about a repository
    a_tags = h3_tag.find_all('a')
    username = a_tags[0].text.strip()
    repo_name = a_tags[1].text.strip()
    repo_url =  base + a_tags[1]['href']
    stars_stars = num_star_count(stars[0].text.strip())
    
    return username, repo_name, stars_stars, repo_url
      

def get_topic_repos(topic_doc):
    #Get all h3 tags containing repo title, repo URL and username
    repo_tags = topic_doc.find_all('h3', class_='f3 color-fg-muted text-normal lh-condensed')
    #Get star tags
    stars = topic_doc.find_all('span', class_ = 'Counter js-social-count')
    
    #Create topic repo Dictionary
    topic_repos_dict ={
        'username' : [],
        'repo_name' : [],
        'stars' : [],
        'repo_url' : []
    }
    
    #Get repo information
    for i in range(len(repo_tags)):
        repo_info = get_repo_info(repo_tags[i], stars[i])
        topic_repos_dict['username'].append(repo_info[0])
        topic_repos_dict['repo_name'].append(repo_info[1])
        topic_repos_dict['stars'].append(repo_info[2])
        topic_repos_dict['repo_url'].append(repo_info[3])
        
    return pd.DataFrame(topic_repos_dict)
        
        
        

     
        
        


# In[ ]:


topic_repos_df = pd.DataFrame(topic_repos_dict)
topic_repos_df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[102]:





# In[103]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





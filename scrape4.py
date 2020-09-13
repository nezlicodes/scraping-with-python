"""
Created on Sat Sep 12 12:30:10 2020

@author: Dell
"""
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
base_url = "https://www.ouedkniss.com/emploi_offres"
url = "https://www.ouedkniss.com/emploi_offres"
jobs = []
npo_jobs = {}
job_no = 0
i = 0
while i<3:
    
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    #Job titles
    job_titles = soup.find_all('h2')
    #Job title counts
#    job_counts = dict()
#    for job in job_titles:
#        job = job.text
#        job_counts[job] = job_counts.get(job, 0) + 1

    jobs = soup.find_all('div', {"class:", "annonce"})
    for job in jobs:
        annonce_titre = job.find('li', {"class:", "annonce_titre"})
        
        title_tag = job.find('h2')
        title = title_tag.text if title_tag else 'N\A'
        
        description_tag = job.find('span', {"class:", "annonce_description_preview"})
        description = description_tag.text if description_tag else "N\A"
        
        domaine_tag = job.find('span', {"class:", "annonce_get_description"})
        field = domaine_tag.text if domaine_tag else "N\A"
       
        wilaya_tag = job.find("span", {"class:", "titre_wilaya"})
        wilaya = wilaya_tag.text if wilaya_tag else "N\A"
        
        link_tag = annonce_titre.find('a').get("href") if annonce_titre else "N\A"
        link = base_url + link_tag if link_tag else "N\A"
        
        job_no+=1
        npo_jobs[job_no] = [title,  description, wilaya, link]

      
    urls = soup.find_all('a', {"class:","page_arrow"})
    if len(urls) == 1:
        url = "https:" + urls[0].get("href")
    else:
        url ="https:" + urls[1].get("href")
    i +=1  


np_job_df = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=['Job title', 'job Description','Wilaya', 'Link'])
print(np_job_df.head())
np_job_df.to_csv('jobs.csv')

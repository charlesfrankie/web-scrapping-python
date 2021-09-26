from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=28').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx' )

filename = 'jobs.csv'
f = open(f'posts/{filename}', 'w')

headers = "Job Position, Company, Required skills, Location, More info\n"
f.write(headers)

for job in jobs:
    job_name = job.header.h2.a.text.strip()
    company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
    more_info = job.header.h2.a['href'].strip()
    ul_tag = job.find('ul', class_ = 'top-jd-dtl clearfix')
    company_location = ul_tag.find('span').text.strip()
    meta_tag = job.find('ul', class_ = 'list-job-dtl clearfix')
    job_description = meta_tag.find('li').text.strip()
    skills = meta_tag.find('span', class_ = 'srp-skills').text.strip()
    if "Freelance" in company_name:
        company_name = "Freelancer"
    if(company_location): 
        f.write(job_name.replace(",", " /") + "," + company_name + "," + skills.replace(",", "|") + "," + company_location + "," + more_info + "\n")
    else:
        f.write(job_name.replace(",", " /") + "," + company_name + "," + skills.replace(",", "|") + "," + "unknown" + "," + more_info + "\n")
print("File Saved")
  


from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=%22Data+Science%22&txtKeywords=%22Data+Science%22%2C&txtLocation="
).text

soup = BeautifulSoup(html_text, "lxml")
job_list = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

companies = []
for job in job_list:
    cmp_name = job.find("h3", class_="joblist-comp-name").text
    companies.append(str(cmp_name).strip())

print(companies)

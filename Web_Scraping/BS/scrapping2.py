from bs4 import BeautifulSoup
import requests


class Scraper:
    def __init__(self):
        html_text = requests.get(
            "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=%22Data+Science%22&txtKeywords=%22Data+Science%22%2C&txtLocation="
        ).text

        self.soup = BeautifulSoup(html_text, "lxml")
        self.job_list = self.soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

        self.companies = []
        self.skills_cmp = []
        self.posted_dates = []

    def scrape(self):
        for job in self.job_list:
            # Scarpping poasted dates
            posted_date = str(
                job.find("span", class_="sim-posted").find("span").text
            ).strip()
            if "month" not in posted_date:
                self.posted_dates.append(posted_date)

                # scrapping companies name
                cmp_name = job.find("h3", class_="joblist-comp-name").text
                self.companies.append(str(cmp_name).strip())

                # scrapping skills list
                skill_span_list = job.find(
                    "div", class_="more-skills-sections"
                ).find_all("span")
                skill_list = [
                    str(span_tag.text).strip() for span_tag in skill_span_list
                ]
                self.skills_cmp.append(skill_list)

    def display_data(self):
        for i, cmp_name in enumerate(self.companies):
            print(f"{cmp_name}")
            print(f"Skill required: {self.skills_cmp[i]}")
            print(f"Posted Date: {self.posted_dates[i]}")
            print("-------")


if __name__ == "__main__":
    scrapper = Scraper()
    scrapper.scrape()
    scrapper.display_data()

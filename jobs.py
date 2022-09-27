from bs4 import BeautifulSoup
import requests
import json

listings = []

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
job_listings = soup.find_all("div", class_="card")
for job in job_listings:
    title = job.find("h2").text
    subtitle = job.find("h3").text
    application_link = job.find("footer").find_all("a", class_="card-footer-item")[1]["href"]
    
    job_dict = {
        "title": title,
        "subtitle": subtitle,
        "application_link": application_link,
    }
    listings.append(job_dict)

json_to_export = json.dumps(listings)
with open("joblistings.json", "w") as f:
    f.write(json_to_export)
    print("Successfully exported job listings data")
    
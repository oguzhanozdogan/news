from bs4 import BeautifulSoup
import requests



url = "https://www.expressen.se/"
response = requests.get(url)
newslist = []
headline = []
soup = BeautifulSoup(response.content, "html.parser")


def expressen_scraper(keyword):
    for articles in soup.find_all("h2"):
        new_headline = articles.contents[0].lower()
        if new_headline not in headline:
            headline.append(new_headline)
        print("Headline: {}".format(articles.text))
        for articles in soup.find_all("div", class_="vignette vignette--text"):
            news_title = articles.contents[0].lower()
            if news_title not in newslist:
                newslist.append(news_title)


    no_of_news = 0
    keyword_list = []
    for i, title in enumerate(headline):
        text = ""
        if keyword.lower() in title:
            text = "<----------KEYWORD"
            no_of_news += 1
            keyword_list.append(title)

        print(i+1, ":", title, text)


        print(f'\n------------Total mentions of "{keyword}" = {no_of_news}------------')
        for i, title in enumerate(keyword_list):
            print(i+1, ":", title)


expressen_scraper(input("Enter your search:"))
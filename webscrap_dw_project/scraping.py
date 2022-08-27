import requests
from bs4 import BeautifulSoup as bs4
import json


def dw_rss():
	article_list = []
	try:
		r = requests.get('https://rss.dw.com/rdf/rss-en-eu')
		soup = bs4(r.content, features='xml')

		articles = soup.findAll('item')
		for a in articles:
			title = a.find('title').text
			link = a.find('link').text
			description = a.find('description').text
			published_date = a.find('dc:date').text
			article = {
				'title': title,
				'link': link,
				'description': description,
				'published_date': published_date
			}
			article_list.append(article)

		return save_articles(article_list)

	except Exception as err:
		print('Scraping failed! Exception: ')
		print(err)


def save_articles(article_list):
	with open('articles.json', 'w') as file:
		json.dump(article_list, file, indent=4)
		

dw_rss()

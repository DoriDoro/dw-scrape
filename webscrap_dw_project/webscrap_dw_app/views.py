from django.shortcuts import render, redirect
from .models import News


def news_list(request):
	news = News.objects.all()
	return render(request, 'news.html', {'news': news})



from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as bs4
import json


def dw_rss(request):
	try:
		r = requests.get('https://rss.dw.com/rdf/rss-en-eu')
		soup = bs4(r.content, features='xml')

		articles = soup.findAll('item')
		for a in articles:
			title = a.find('title').text
			link = a.find('link').text
			description = a.find('description').text
			published_date = a.find('dc:date').text

			article = News()
			article = {
				'title': title,
				'link': link,
				'description': description,
				'published_date': published_date
			}
			article.save()

		return redirect(save_articles)

	except Exception as err:
		print('Scraping failed! Exception: ')
		print(err)


def save_articles(request):
	news = News.objects.all()
	return render(request, 'news.html', {'news':news})
		




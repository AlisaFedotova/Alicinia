import re
import requests

siteUrl = 'http://www.csd.tsu.ru'

n = 3
uniqEmails = set()
uniqUrls = set()

def emailSearch(url, depth):
	if depth <= n:
		try:
			request = requests.get(url)
		except:
			return
		currEmails=re.findall(r'[a-z][\w]*[@][a-z][\w]*[\.][a-z][\w|.]*', request.text)
		for em in currEmails:
			uniqEmails.add(em)

		absUrl=re.findall(r'href="(http?:\/\/[\w\/\.]*)"', request.text)
		relUrl=re.findall(r'href=[\"\'](.*?)[\"\']', request.text)
		for url in absUrl:
			if url not in uniqUrls:
				uniqUrls.add(url)
				emailSearch(url, depth + 1)

		for url in relUrl:
			if url not in uniqUrls:
				uniqUrls.add(url)
				emailSearch(url, depth + 1)



emailSearch(siteUrl, 1)
print('result: ')
print(uniqEmails)

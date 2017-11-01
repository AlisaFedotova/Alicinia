import re
import requests

passPages = set()
needEmails = set()

siteUrl = 'http://www.tsu.ru'

n = 100 
uniqEmails = []

def emailSearch(depth):
  currEmail=set(re.findall(r'[a-z][\w]*[@][a-z][\w]*[\.][a-z][\w|.]*')
  for i in range(n):
      if (currEmail!=uniqEmails[i]):
        uniqEmails.append(currEmail)
      elif uniqEmails[i]==currEmail:
          i=i-1
          break
  needEmails.update(currEmail)
  if depth>0:
    absUrl=set(re.findall(r' <a href="(http?:\/\/[\w\/\.]*)">'))
    relUrl=set(re.findall(r' <a href="([\"\']([^\"\']*)[\"\'])">'))
    absUrl.update(siteUrl+x for x in relUrl)
    for i in relUrl.difference(passPages):
      emailSearch(i,depth-1)

    
emailSearch(1)
print('result: ')
print(uniqEmails)

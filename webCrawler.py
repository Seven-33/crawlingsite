from urllib.parse import urldefrag
from wsgiref import headers
import requests
import lxml
from bs4 import BeautifulSoup
from xlwt import*
workbook = Workbook()
table = workbook.add_sheet('data')
# Create the header of each column in the first row.
table.write(0, 0, 'Number')
table.write(0, 1, 'site_url')
table.write(0, 2, 'site_name')
line=1

url = "https://kinsta.com/blog/wordpress-site-examples/"
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
} 
f=requests.get(url, headers=headers)
soup= BeautifulSoup(f.content, 'lxml')
sites_list = []
sites = soup.find_all('a')
num=0
for anchor in sites:
  rel=anchor.get('rel')
  if anchor.string:
    print(anchor.string)
    if rel:
      if "noopener" in rel and "noreferrer" in rel:
        urls= anchor['href']
        sites_list.append(urls)
        num +=1
        print(num, urls, '\n', 'Best Wordpress sites:'+ anchor.string.strip())

        # Write the crawled data into Excel separately from the second row.
        table.write(line, 0, num)
        table.write(line, 1, urls)
        table.write(line, 2, anchor.string.strip())
        line += 1
        workbook.save('best_sites.xls')
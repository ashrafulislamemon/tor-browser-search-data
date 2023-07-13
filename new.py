import nltk   
from urllib3 import urlopen

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"    
html = urlopen(url).read()    
raw = nltk.clean_html(html)  
print(raw)
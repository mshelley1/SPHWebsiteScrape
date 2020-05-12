# From https://realpython.com/python-web-scraping-practical-introduction/
# In shell: pip install requests BeautifulSoup4

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)
    
raw_html = simple_get('https://realpython.com/blog/')
len(raw_html)


# Mathemetician example
raw_html = simple_get('http://www.fabpedigree.com/james/mathmen.htm')
html = BeautifulSoup(raw_html, 'html.parser')
for i, li in enumerate(html.select('li')):
        print(i, li.text)


# Try with SPH
raw_html = simple_get('https://sph.umd.edu/content/admissions')
soup = BeautifulSoup(raw_html, 'html.parser')
print(soup.prettify())
list(soup.children)
[type(item) for item in list(soup.children)]
html = list(soup.children)[2]
body = list(html.children)[3]


soup.find_all('p')  # This is the key 



for i, li in enumerate(html.select('li')):
        print(i, li.text)











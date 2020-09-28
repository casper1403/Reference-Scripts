html_doc = """
<html><head><title name="henk">The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p> This is a second p tag </p>
<p class="story">...</p>
"""

"""
Instruction from:        https://www.pluralsight.com/guides/extracting-data-html-beautifulsoup

Steps for Scraping Any Website:


        - Sending an HTTP GET request to the URL of the webpage that you want to scrape, which will respond with HTML content. We can do this by using the Request library of Python.

        - Fetching and parsing the data using Beautifulsoup and maintain the data in some data structure such as Dict or List.

        - Analyzing the HTML tags and their attributes, such as class, id, and other HTML tag attributes. Also, identifying your HTML tags where your content lives.

        - Outputting the data in any file format such as CSV, XLSX, JSON, etc.

"""


from bs4 import BeautifulSoup
import requests

url = 'https://www.google.nl/'
get_request = requests.get(url).text
soup = BeautifulSoup(get_request,'html.parser')


"""

INTRODUCTION:

BeautifulSoup is a python library used for scraping data from a html page.  In this handbook the html code above is used as an example

in real life you would parse the html through a request which is also shown abovs

 Some simple ways to navigate the data structure"""


soup = BeautifulSoup(html_doc, 'html.parser')

# Make the html page look more pretty
soup.prettify()


# get the title tag of the html
soup.title

#GET all the text from a html page
soup.get_text()

# Get the name defines in the tag
soup.title.name

#get the text in the title
soup.title.text

# Get the text in string format
soup.title.string

#Get the parent tag of the object
soup.title.parent.name

#Get the first p tag
soup.p

# get the class of the p tag
soup.p['class']

#get the first a tag
soup.a

#return all a tags in a list
soup.find_all('a')

# return single element
soup.find(id='link3')

# search for a class
soup.find_all("tag", {"class":"class_name"})


# """ To get all the elements with the find_all function is to use a for loo[]"""
for link in soup.find_all('a'):
    link.get('href')



"""
BEAUTIFULSOUP OBJECTS PARSED FROM THE GET REQUEST

documentation:
    'Beautiful Soup transforms a complex HTML document into a complex tree of Python objects.
        But you’ll only ever have to deal with about four kinds of objects:
        -Tag
        -NavigableString
        -BeautifulSoup
        -Comment'
"""


"""           NAVIGATING THE TREE   : using the code above

        Tags may contain strings and other tags. These elements are the tag’s children. Beautiful Soup provides a lot of different attributes for navigating and iterating over a tag’s children.                   """



# The simplest way to navigate the parse tree is to say the name of the tag you want. If you want the <head> tag, just say soup.head:
soup.head
# <head><title>The Dormouse's story</title></head>

soup.title
# <title>The Dormouse's story</title>


# You can do use this trick again and again to zoom in on a certain part of the parse tree. This code gets the first <b> tag beneath the <body> tag:
soup.body.b
# <b>The Dormouse's story</b>


# Using a tag name as an attribute will give you only the first tag by that name:
soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>


# If you need to get all the <a> tags, or anything more complicated than the first tag with a certain name, you’ll need to use one of the methods described in Searching the tree, such as find_all():
soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


# You can acces the childeren of a tag by calling .contents    A string never has contents
soup.head.contents

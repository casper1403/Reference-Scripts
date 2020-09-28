#!/usr/bin/env python
# Name:
# Student number:
"""
This script crawls the IMDB top 250 movies.
"""

import os
import csv
import codecs
import errno
import time
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

# global constants
TOP_250_URL = 'http://www.imdb.com/chart/top'
OUTPUT_CSV = 'top250movies.csv'
SCRIPT_DIR = os.path.split(os.path.realpath(__file__))[0]
BACKUP_DIR = os.path.join(SCRIPT_DIR, 'HTML_BACKUPS')

# --------------------------------------------------------------------------
# Utility functions (no need to edit):


def create_dir(directory):
    """
    Create directory if needed.
    Args:
        directory: string, path of directory to be made
    Note: the backup directory is used to save the HTML of the pages you
        crawl.
    """

    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno == errno.EEXIST:
            # Backup directory already exists, no problem for this script,
            # just ignore the exception and carry on.
            pass
        else:
            # All errors other than an already existing backup directory
            # are not handled, so the exception is re-raised and the
            # script will crash here.
            raise


def save_csv(filename, rows):
    """
    Save CSV file with the top 250 most popular movies on IMDB.
    Args:
        filename: string filename for the CSV file
        rows: list of rows to be saved (250 movies in this exercise)
    """
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'title', 'year', 'runtime', 'genre(s)', 'director(s)', 'writer(s)',
            'actor(s)', 'rating(s)', 'number of rating(s)'
        ])

        writer.writerows(rows)


def make_backup(filename, html):
    """
    Save HTML to file.
    Args:
        filename: absolute path of file to save
        html: (unicode) string of the html file
    """

    with open(filename, 'wb') as f:
        f.write(html)


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        print('The following error occurred during HTTP GET request to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def main():
    """
    Crawl the IMDB top 250 movies, save CSV with their information.
    Note:
        This function also makes backups of the HTML files in a sub-directory
        called HTML_BACKUPS (those will be used in grading).
    """

    # Create a directory to store copies of all the relevant HTML files (those
    # will be used in testing).
    print('Setting up backup dir if needed ...')
    create_dir(BACKUP_DIR)

    # Make backup of the IMDB top 250 movies page
    print('Access top 250 page, making backup ...')
    top_250_html = simple_get(TOP_250_URL)
    top_250_dom = BeautifulSoup(top_250_html, "lxml")

    make_backup(os.path.join(BACKUP_DIR, 'index.html'), top_250_html)

    # extract the top 250 movies
    print('Scraping top 250 page ...')
    url_strings = scrape_top_250(top_250_dom)

    # grab all relevant information from the 250 movie web pages
    rows = []
    for i, url in enumerate(url_strings):  # Enumerate, a great Python trick!
        print('Scraping movie %d ...' % i)

        # Grab web page
        movie_html = simple_get(url)
        # Extract relevant information for each movie
        movie_dom = BeautifulSoup(movie_html, "lxml")

        rows.append(scrape_movie_page(movie_dom))

        # Save one of the IMDB's movie pages (for testing)
        if i == 83:
            html_file = os.path.join(BACKUP_DIR, 'movie-%03d.html' % i)
            make_backup(html_file, movie_html)

    # Save a CSV file with the relevant information for the top 250 movies.
    print('Saving CSV ...')
    save_csv(os.path.join(SCRIPT_DIR, 'top250movies.csv'), rows)


# --------------------------------------------------------------------------
# Functions to adapt or provide implementations for:

def scrape_top_250(soup):
    """
    Scrape the IMDB top 250 movies index page.
    Args:
        soup: parsed DOM element of the top 250 index page
    Returns:
        A list of strings, where each string is the URL to a movie's page on
        IMDB, note that these URLS must be absolute (i.e. include the http
        part, the domain part and the path part).
    """
    movie_urls = []
    # Find the class that lists the movies. Save the table in a variable. Take all the td elements. Add the urls to a list and return
    movie_object = soup.find("div",{"class":"lister"})
    table_body_object = movie_object.tbody
    titles = table_body_object.find_all("td",{"class":"titleColumn"})
    for title in titles:
        movie_urls.append(f"https://www.imdb.com/{title.a.get('href')}")
    return movie_urls


def scrape_movie_page(dom):
    """
    Scrape the IMDB page for a single movie
    Args:
        dom: BeautifulSoup DOM instance representing the page of 1 single
            movie.
    Returns:
        A list of strings representing the following (in order): title, year,
        duration, genre(s) (semicolon separated if several), director(s)
        (semicolon separated if several), writer(s) (semicolon separated if
        several), actor(s) (semicolon separated if several), rating, number
        of ratings.
    """
    # get the title
    title = dom.h1.text[:-7]
    title = title.replace("\xa0","")
    #get the year
    year = dom.h1.text[-6:-2]
    # Get the durations
    duration = dom.time.text[24:33]
    if "\n" in duration:
        duration = duration.replace("\n","")

    #Get the genre
    genre = dom.find("div",{"class":"subtext"})
    genre = genre.find_all("a")
    del genre[-1]
    genre_list = []
    if len(genre) > 1:
        for gen in genre:
            genre_list.append(gen.text)
    else:
        genre = genre[0].text
    if genre_list:
        genre = ";".join(genre_list)

    #Get the rating
    rating_object = dom.find("div",{"class":"ratingValue"})
    rating = rating_object.strong.text

    # Get the number of ratings
    number_rating_object = dom.find("span",{"class":"small"})
    number = number_rating_object.text
    number = number.replace(",",".")

    # Get the director
    directors_object = dom.find("div",{"class":"credit_summary_item"}).text[11:]
    directors = directors_object.replace(",",";")

    #Fetch the object containing writers and actors
    witers_stars_object = dom.find_all("div",{"class":"credit_summary_item"})
    object_text = []
    for object in witers_stars_object:
        texts = object.text
        texts = texts.replace("\n","")
        object_text.append(texts)

    #Get the writers
    writers = object_text[1]
    writers = writers[8:]
    if "|" in writers:
        writers = writers[:writers.index("|")]
    if "(" in writers:
        writers = writers.replace(f'{writers[writers.find("(")+1:writers.find(")")]}',"")
        writers = writers.replace("(screenplay)","")
        writers = writers.replace("()","")
        writers = writers.replace("   ","")
    if "," in writers:
        writers = writers.replace(",",";")

    # Get the actors
    actors = object_text[2]
    actors = actors[6:]
    if "|" in actors:
        actors = actors[:actors.index("|")]
    if "(" in actors:
        actors = actors.replace(f'{actors[actors.find("(")+1:actors.find(")")]}',"")
        actors = actors.replace("(screenplay)","")
        actors = actors.replace("   ","")
    if "," in actors:
        actors = actors.replace(",",";")


    return [title,year,duration,genre,directors,writers,actors,rating,number]



if __name__ == '__main__':
    main()  # call into the progam

    # If you want to test the functions you wrote, you can do that here:
    # ...

# -*- coding: utf-8 -*-

import csv
import requests

def fetch_all():
    index = 1
    size = 10
    with open('output/quotes.csv', 'wb') as csvfile:
        quoteswriter = csv.writer(csvfile)
        while True:
            posts = get_posts(size, index)
            for post in posts:
                print post
                quoteswriter.writerow([post['ID'], post['title'].encode('utf-8'), get_text(post['content']), post['link']])
            if len(posts) == 0 or len(posts) < size:
                break
            index += 1


def get_text(html):
    s = html.replace('<p>', '').replace('</p>', '').encode('utf-8')
    return s


def get_posts(size, page):
    url = 'http://quotesondesign.com/wp-json/posts?filter[orderby]=time&filter[posts_per_page]=%d&page=%d' %(size, page)
    r = requests.get(url)
    return r.json()


if __name__ == '__main__':
    fetch_all()

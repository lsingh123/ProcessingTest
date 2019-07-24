#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 12:58:07 2019

@author: lavanyasingh
"""

from multiprocessing import Pool
from bs4 import BeautifulSoup
import csv
from requests_html import HTMLSession

class FBOGCrawler():
    
    PATH = "/Users/lavanyasingh/Desktop/GSC2O19internet_archive/data/raw/"
    
    def __init__(self, processes, num_urls, urls):
        self.urls = urls
        self.results = []
        self.session = HTMLSession()
        self.processes = processes
        self.num_urls = num_urls
        
    def read_in(self):
        urls = []
        with open(self.PATH + "all_raw_cleaned3.csv", 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for line in reader:
                if len(self.urls) > self.num_urls: break
                self.urls.append("http://" + "".join(line[1]))
        print("DONE READING")
        return urls
    
    def get_attr(self, head, attr):
        try:
            return head.find(attrs={"property": "og:" + attr})['content']
        except TypeError:
            pass
        try:
            return head.find(attrs={"property": "twitter:" + attr})['content']
        except TypeError:
            pass
        try:
            return head.find("title").text
        except AttributeError:
            return ""
    
    def get_locale(self, head):
        try: 
            return head.find(attrs={"property": "og:locale"})['content']
        except TypeError:
            return ""
    
    def get_meta(self, url):
        try:
            response = self.session.get(url, timeout = 30)
            soup = BeautifulSoup(response.html.html, features = "html.parser")
            head = soup.head
            title = self.get_attr(head, "title")
            desc = self.get_attr(head, "description")
            locale = self.get_locale(head)
            return [url, title, desc, locale]
        except Exception as e:
            return [url, str(e)]
    
    def write_meta(self):
        with open(self.PATH + "meta_good.csv", 'w') as outf:
            w = csv.writer(outf, delimiter= ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
            for url in self.res:
                w.writerow(url)
        print("WROTE ALL META")
    
    def main(self):
        #we want to test how many processes is the ideal number
        p = Pool(processes=self.processes)
        self.res = p.map(self.get_meta, self.urls)
        p.close()
        p.join()
        self.session.close()


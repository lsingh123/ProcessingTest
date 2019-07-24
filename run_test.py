#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:08:28 2019

@author: lavanyasingh
"""

from script import FBOGCrawler
import timeit
import matplotlib.pyplot as plt

def run_script(processes, urls):
    crawler = FBOGCrawler(processes, 1, urls)
    time = timeit.timeit(crawler.main, number = 100)
    print(f"Time:{time:.5f}", time)
    return time

def get_urls():
    crawler = FBOGCrawler(1, 5, [])
    return crawler.read_in()

def test_processes(max_processes):
    urls = get_urls()
    times = [run_script(i, urls) for i in range(1, max_processes+1)]
    plt.plot(range(1, max_processes+1), times)
    plt.ylabel('time')
    plt.xlabel('processes')
    plt.show()

if __name__ == "__main__":
    test_processes(20)
    

    
    
    
    
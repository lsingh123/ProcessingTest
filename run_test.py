#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:08:28 2019

@author: lavanyasingh
"""

from script import FBOGCrawler
import timeit
import matplotlib.pyplot as plt

def run_script(processes):
    crawler = FBOGCrawler(processes, 2)
    time = timeit.timeit(crawler.main, number = 5)
    print(time)
    return time

def test_processes(max_processes):
    times = [run_script(i) for i in range(3, max_processes+1)]
    plt.plot(range(1, max_processes+1), times)
    print("MIN:", min(times), times.index(min(times)))
    plt.ylabel('time')
    plt.xlabel('processes')
    plt.show()

if __name__ == "__main__":
    test_processes(20)
    
    
    
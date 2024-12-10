from time import time_ns
from typing import Type

from Scripts.scraper import Scraper

def timer(scraper: Scraper) -> int:
    start = time_ns()
    scraper.scrape()
    end = time_ns()
    
    return end - start
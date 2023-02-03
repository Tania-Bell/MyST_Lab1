# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:51:46 2023

@author: Tania
"""

import functions as fn
from data import all_files

common_tickers, all_files = fn.find_tickers(all_files,'Ticker')
print(common_tickers)
print(all_files)

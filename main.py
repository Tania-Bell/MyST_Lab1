# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:51:46 2023

@author: Tania
"""

import functions as fn
from data import all_files


print(fn.find_tickers(all_files,'Ticker'))
print(len(fn.find_tickers(all_files,'Ticker')))
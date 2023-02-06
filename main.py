# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:51:46 2023

@author: Tania
"""

import functions as fn
from data import all_files

common_tickers, all_files = fn.find_tickers(all_files,'Ticker','Peso (%)')

prices=fn.import_prices(all_files,common_tickers,'2021-01-29','2023-01-26')

cash_w=float(all_files['20210129'][all_files['20210129']['Ticker'].str.contains("MXN")]['Peso (%)'])
cap_shares = fn.shares(all_files,prices,cash_w,'20210129')

returns_ticker, returns_monthly = fn.rend(prices,cap_shares,cash_w)

print(returns_monthly)
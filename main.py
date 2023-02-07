# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:51:46 2023

@author: Tania
"""

import functions as fn
from data import all_files
import pandas as pd

all_files = fn.import_files('files/*.csv')

common_tickers, all_files = fn.find_tickers(all_files,'Ticker','Peso (%)')

prices=fn.import_prices(all_files,common_tickers,'2021-01-29','2023-01-26')

cash_w=float(all_files['20210129'][all_files['20210129']['Ticker'].str.contains("MXN")]['Peso (%)'])

cap_shares_p = fn.shares_passive(all_files,prices,cash_w,'20210129')

returns_ticker_p, df_pasiva = fn.rend_p(prices,cap_shares_p,cash_w)

rf=.1106

weights = fn.sharpe(prices,rf)

cap_shares_a = fn.shares_active(weights, prices, cash_w, '20210129')

shares_rebal_a = fn.rebalance(prices,cap_shares_a,0.05,0.025)

df_activa = fn.rend_a(cap_shares_a,prices,cash_w)

comission_rate = 0.00125

comission_monthly = fn.comission(comission_rate,prices,shares_rebal_a)

df_operaciones = fn.operations(shares_rebal_a,comission_rate,prices,comission_monthly)


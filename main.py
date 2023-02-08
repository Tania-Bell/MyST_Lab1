# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:51:46 2023

@author: Tania
"""

import functions as fn
from data import all_files
import pandas as pd

comission_rate = 0.00125

rf=.1106

r_change = 0.05

r_rebalance = 0.025

all_files = fn.import_files('files/*.csv')

common_tickers, all_files = fn.find_tickers(all_files,'Ticker','Peso (%)')

prices=fn.import_prices(all_files,common_tickers,'2021-01-29','2023-01-26')

cash_w=float(all_files['20210129'][all_files['20210129']['Ticker'].str.contains("MXN")]['Peso (%)'])

cap_shares_p = fn.shares_passive(all_files,prices,cash_w,'20210129').round()

comission_p = fn.comission_p(comission_rate,prices,cap_shares_p,'20210129')

returns_ticker_p, df_pasiva = fn.rend_p(prices,cap_shares_p,cash_w)

prices_daily = fn.import_prices_d(common_tickers,'2021-01-31','2022-01-31')

weights = fn.sharpe(prices_daily,rf)

cap_shares_a = fn.shares_active(weights, prices, cash_w, '20210129').round()

capital_hist, shares_hist, comission_hist, shares_diff_hist = fn.rebalanceo(cash_w,cap_shares_a,prices,r_change,r_rebalance,comission_rate)

df_activa = fn.rend_a(capital_hist,cash_w)

df_operaciones = fn.operations(shares_hist,comission_hist,shares_diff_hist)
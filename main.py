# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:51:46 2023

@author: Tania
"""

from data import nt_1, nt_2, nt_3, nt_4, nt_5, nt_6, nt_7, \
    nt_8, nt_9, nt_10, nt_11, nt_12, nt_13, nt_14, nt_15, \
    nt_16, nt_17, nt_18, nt_19, nt_20, nt_21, nt_22, nt_23, \
    nt_24, nt_25

common_tickers = set(nt_1['Ticker'].values).intersection(set(nt_2['Ticker'].values))\
                    .intersection(set(nt_3['Ticker'].values))\
                    .intersection(set(nt_4['Ticker'].values))\
                    .intersection(set(nt_5['Ticker'].values))\
                    .intersection(set(nt_6['Ticker'].values))\
                    .intersection(set(nt_7['Ticker'].values))\
                    .intersection(set(nt_8['Ticker'].values))\
                    .intersection(set(nt_9['Ticker'].values))\
                    .intersection(set(nt_10['Ticker'].values))\
                    .intersection(set(nt_11['Ticker'].values))\
                    .intersection(set(nt_12['Ticker'].values))\
                    .intersection(set(nt_13['Ticker'].values))\
                    .intersection(set(nt_14['Ticker'].values))\
                    .intersection(set(nt_15['Ticker'].values))\
                    .intersection(set(nt_16['Ticker'].values))\
                    .intersection(set(nt_17['Ticker'].values))\
                    .intersection(set(nt_18['Ticker'].values))\
                    .intersection(set(nt_19['Ticker'].values))\
                    .intersection(set(nt_20['Ticker'].values))\
                    .intersection(set(nt_21['Ticker'].values))\
                    .intersection(set(nt_22['Ticker'].values))\
                    .intersection(set(nt_23['Ticker'].values))\
                    .intersection(set(nt_24['Ticker'].values))\
                    .intersection(set(nt_25['Ticker'].values))
                    
print(common_tickers)
print(len(common_tickers))
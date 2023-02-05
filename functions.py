# -*- coding: utf-8 -*-"""Created on Mon Jan 30 19:50:15 2023@author: Tania"""# python3 -m venv venv/ import pandas as pdimport pathlibimport globfrom os import listdirfrom os.path import isfile, joinimport numpy as npimport pandas_datareader.data as webfrom scipy.optimize import minimizeimport yfinance as yfdef import_files(path):    """ This function imports all files in folder given the folder path.    It ignores the first two rows and sorts the Tickers in alphabetical order."""    files = list(glob.glob(path))    all_files = {}    for i in files:        data = pd.read_csv(i, skiprows=2).iloc[:-1 , :]        all_files[i[14:22]] = data[['Ticker', 'Peso (%)']]    for i in range(0, len(all_files.keys())):        all_files[list(all_files.keys())[i]]=all_files[list(all_files.keys())[i]].sort_values('Ticker')    return all_filesdef find_tickers(datos,columna_ticker,columna_pesos):    """Given a dictionary comprised of dataframes, the column of the Tickers and the column of the weights,    this function will clean the tickers of any unwanted characters. It then adds the '.MX' suffix    and then filters each dataframe so that the only tickers that appear are the ones that the dataframes have in common.    Finally, the function accumulates the weights of the rows that were filtered out and adds them to CASH (MXN)"""    for i in range(0, len(datos.keys())):        datos[list(datos.keys())[i]][columna_ticker] = datos[list(datos.keys())[i]][columna_ticker].str.replace("*", "").str.replace(            ".", "-")    for i in range(0, len(datos.keys())):        datos[list(datos.keys())[i]][columna_ticker] = datos[list(datos.keys())[i]][columna_ticker].map('{}.MX'.format)    for i in range(0,len(datos.keys())-1):        if i==0:            common_tickers = datos[list(datos.keys())[i]][columna_ticker]        else:            common_tickers = set(common_tickers).intersection(set(datos[list(datos.keys())[i+1]][columna_ticker].values))    for i in range(0, len(datos.keys())):        datos[list(datos.keys())[i]] = datos[list(datos.keys())[i]].drop(            datos[list(datos.keys())[i]].index[~datos[list(datos.keys())[i]][columna_ticker].isin(common_tickers)])    for i in range(0,len(datos.keys())):        acum = sum(datos[list(datos.keys())[i]][columna_pesos][~datos[list(datos.keys())[i]][columna_ticker].str.contains('MXN')])        datos[list(datos.keys())[i]][columna_pesos][datos[list(datos.keys())[i]][columna_ticker].str.contains('MXN')] = 100 - acum    return common_tickers, datosdef import_prices(datos,tickers,start_date,end_date):    """ Removes the CASH of the list of tickers then imports Adj Close from    yfinance of list of tickers. Then formats date and transposes"""    tickers = list(filter(lambda k: 'MXN' not in k, tickers))    prices = yf.download(tickers, start=start_date, end=end_date)['Adj Close']    prices.index = prices.index.strftime('%Y%m%d')    prices = prices.filter(items=datos.keys(), axis=0)    prices=prices.transpose()    return pricesdef titles(datos, precios, cash_weight,start_date):    """Returns a single column which has the amount of shares of each ticker."""    titulos = pd.DataFrame()    datos[start_date] = datos[start_date][~datos[start_date]['Ticker'].str.contains("MXN")]    titulos[start_date] = ((1000000 - (1000000 * cash_weight/100)) * datos[start_date]['Peso (%)']/100).to_numpy()/precios.loc[:,start_date].to_numpy()    titulos.index = precios.index    return titulosdef rend(precios, titulos, cash_weight):    """Returns two dataframes. The first one is the capital in pesos at each date.    The second one is a dataframe with a column of the total capital (with cash)    at each date, the second one is the logarithmic returns between each month and    the third one is the cumulative returns."""    rend_ticker = pd.DataFrame()    rend_mensual = pd.DataFrame()    for i in precios.columns:        rend_ticker[i] = titulos.iloc[:,0].to_numpy() * precios.loc[:,i].to_numpy()    for i in rend_ticker.columns:        rend_mensual[i] = [sum(rend_ticker.loc[:,i]) + (1000000 * cash_weight/100)]    rend_mensual = rend_mensual.transpose()    rend_mensual = rend_mensual.rename(columns={0: "Capital"})    rend_mensual['Returns'] = 0    rend_mensual['Returns']=rend_mensual['Returns'].astype(float)    for i in range(0,len(rend_mensual)-1):        rend_mensual['Returns'][i] = np.log(rend_mensual['Capital'][i+1]/rend_mensual['Capital'][i])    rend_mensual['Cumulative Returns'] = rend_mensual['Returns'].cumsum()    return rend_ticker, rend_mensual
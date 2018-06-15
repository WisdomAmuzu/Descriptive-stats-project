import csv
import numpy as np
from math import sqrt

def data_retriever(file):
    with open(file, 'r') as f:
        data_dict = dict()
        reader = csv.reader(f)
        dates = []
        opns = []
        highs = []
        lows = []
        closes = []
        adj_closes = []
        volumes = []
        for date, opn, high, low, close, adj_close, volume in reader:
            try:
                dates.append(date)
                opns.append(float(opn))
                highs.append(float(high))
                lows.append(float(low))
                closes.append(float(close))
                adj_closes.append(float(adj_close))
                volumes.append(float(volume))
            except ValueError:
                continue
        data_dict['dates'] = dates[1:]
        data_dict['opens'] = opns[1:]
        data_dict['closes'] = closes[1:]
        data_dict['high'] = highs[1:]
        data_dict['low'] = lows[1:]
        data_dict['adj_closes'] = adj_closes[1:]
        data_dict['volume'] = volumes[1:]
    return data_dict


def cols():
    data = data_retriever('JPM.csv')
    x = np.array(data.get('opens'))
    y = np.array(data.get('closes'))
    return (x, y)


def avg_s_v():
    x, y = cols()
    sum_of_opens = np.sum(x)
    sum_of_closes = np.sum(y)
    avg_s_val = (sum_of_closes - sum_of_opens) * 0.5
    return round(avg_s_val, 2)


def stock_volatility():
    data = data_retriever('JPM.csv')
    x = data.get('opens')
    y = data.get('closes')
    l = np.array([i * j for i in x for j in y])
    std = np.std(l)
    return round(std, 2)


def daily_stock_returns():
    x, y = cols()
    sigma_open = np.sum(x)
    sigma_close = np.sum(y)
    n_o_shares = avg_s_v()
    d_s_returns = (sigma_close - sigma_open) * n_o_shares
    return round(d_s_returns, 2)


def main():
    print('Average stock value = {}'.format(avg_s_v()))
    print('Stock Volatility = {}'.format(stock_volatility()))
    print('Daily stock returns = {}'.format(daily_stock_returns()))


if __name__ == '__main__':
    main()

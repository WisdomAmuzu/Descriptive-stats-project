import numpy as np
import csv

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


def estimate_coef(x, y):
    n = np.size(x)

    m_x, m_y = np.mean(x), np.mean(y)

    sigma_xy = np.sum(y * x - n * m_y * m_x)
    sigma_xx = np.sum(x * x - n * m_x * m_x)
    b_1 = sigma_xy / sigma_xx
    b_0 = m_y - b_1 * m_x
    return(b_0, b_1)


def main(data):
    x = np.array(data.get('opens'))
    y = np.array(data.get('closes'))

    b = estimate_coef(x, y)
    return b


if __name__ == '__main__':
    reg = main(data_retriever('JPM.csv'))
    print('Regression = {}'.format(reg))

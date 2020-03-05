import numpy as np
import json

def compute_error(p1, p2, x_data, y_data):
    mse = 0
    mae = 0
    for i in range(0, len(x_data)):
        mse += (y_data[i] - (p2 * x_data[i] + p1)) ** 2
        mae += abs(y_data[i] - (p2 * x_data[i] + p1))
    return (int(mse / len(x_data)), int(mae / len(x_data)))

try:
    with open('variables.json') as f:
        p_dict = json.load(f)
        p1 = p_dict['p1']
        p2 = p_dict['p2']       
    data = np.genfromtxt('data.csv', delimiter = ',') 
    x_data = data[1: , 0]
    y_data = data[1: , 1]       
    print('Before training p1 = {0}, p2 = {1}, Mean square error = {2}, Mean absolute error = {3}'.format(0, 0, compute_error(0, 0, x_data, y_data)[0], compute_error(0, 0, x_data, y_data)[1]))
    print('After training p1 = {0}, p2 = {1}, Mean square error = {2}, Mean absolute error = {3}'.format(p1, p2, compute_error(p1, p2, x_data, y_data)[0], compute_error(p1, p2, x_data, y_data)[1]))
except FileNotFoundError:
    print('Please run training program first!')

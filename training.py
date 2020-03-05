import numpy as np
import matplotlib.pyplot as plt
import json

p1 = 0
p2 = 0
lr = 0.05
epochs = 4001
data = np.genfromtxt('data.csv', delimiter = ',')
x_data = data[1: , 0]
max_xdata = np.max(x_data)
min_xdata = np.min(x_data)
max_min_xdata = max_xdata - min_xdata
x_data_n = (x_data - min_xdata) / max_min_xdata
y_data = data[1: , 1]
max_ydata = np.max(y_data)
min_ydata = np.min(y_data)
max_min_ydata = max_ydata - min_ydata
y_data_n = (y_data - min_ydata) / max_min_ydata

def graph(x_data, y_data, p1, p2):
    l1, = plt.plot(x_data, y_data, 'b.')
    l2, = plt.plot(x_data, p2 * x_data + p1, 'r')
    plt.legend(handles=[l1,l2], labels=['Training dataset', 'Linear regression'], loc='best')
    plt.title('Linear regression to predict the price of a car for a given mileage')

def gradient_decent_runner(x_data_n, y_data_n, p1, p2, lr, epochs):
    m = len(x_data_n)
    for i in range(epochs):
        p1_grad = 0
        p2_grad = 0
        for j in range(0, m):
            p1_grad += (((p2 * x_data_n[j]) + p1) - y_data_n[j]) / m
            p2_grad += x_data_n[j] * (((p2 * x_data_n[j]) + p1) - y_data_n[j]) / m
        p1 = p1 - (lr * p1_grad)
        p2 = p2 - (lr * p2_grad)
        if i % 500 == 0:
            #print('epochs:', i)
            plt.ion()
            plt.figure()
            plt.xlabel('km normalized')
            plt.ylabel('price normalized')
            graph(x_data_n, y_data_n, p1, p2)
            plt.text(0.8,0.8, r'$epochs:\ %s$' %i)
            plt.show()
            plt.pause(1)
            plt.close()      
    p1 = p1 * max_min_ydata + min_ydata - min_xdata * p2 * max_min_ydata / max_min_xdata    
    p2 = p2 * max_min_ydata / max_min_xdata
    return p1, p2         

print('Starting p1 = {0}, p2 = {1}'.format(p1, p2))
print('Running...')
p1, p2 = gradient_decent_runner(x_data_n, y_data_n, p1, p2, lr, epochs)
p_dict = {'p1':p1, 'p2':p2}
with open('variables.json', 'w') as f:
    json.dump(p_dict,f)
print('After {0} iterations p1 = {1}, p2 = {2}'.format(epochs, p1, p2))
plt.figure(figsize = (10, 7))
plt.xlabel('km')
plt.ylabel('price')
graph(x_data, y_data, p1, p2)
plt.text(140000,7000, 'Training completed,\nPlease close the window to continue', fontsize = 12, weight = 'bold')
plt.ioff()
plt.show()

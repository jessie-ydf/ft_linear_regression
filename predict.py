import json

if __name__=='__main__':
    p1 = 0
    p2 = 0
    mileage = ''
    while mileage.isnumeric() == False:
        mileage = input('Please input an integer mileage to estimate the price of a car:\n')
    mileage = int(mileage)
    try:
        with open('variables.json') as f:
            p_dict = json.load(f)
            p1 = p_dict['p1']
            p2 = p_dict['p2']
        price = round(p1 + (p2 * mileage))
        if price < 0:
            price = 0
        print('The price esmated is:\n'+str(price)+'\n')
    except FileNotFoundError:
        print('Please run training program first!')

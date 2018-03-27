import csv


buy_map = {}
sell_map = {}

quantities = []
prices = []


class Gdax:
    price = ''
    quantity = ''
    total = ''

def calculate(file_location):
    #fill the maps with the actual data
    with open(file_location, 'r') as gdax_file:
        reader = csv.reader(gdax_file)
        i = 0
        for row in reader:
            if i==0:
                i = i + 1
                continue
            type = row[2]
            gdax = Gdax()
            gdax.price = row[6]
            gdax.quantity = row[4]
            gdax.date = row[3]
            gdax.total = row[8]
            if type == 'BUY':
                buy_map[row[0]] = gdax
            elif type == 'SELL':
                sell_map[row[0]] = gdax
            print(row)


def calculate_v2 (file_location):
    gains_or_loss_2017 = 0
    with open(file_location, 'r') as gdax_file:
        reader = csv.reader(gdax_file)
        i = 0
        for row in reader:
            if i==0:
                i = i + 1
                continue
            type = row[2]
            if type == 'BUY':
                quantities.append(float(row[4]))
                prices.append(float(row[6]))
            elif type == 'SELL':
                quantity = float(row[4])
                orig_quantity = quantity
                price = float(row[6])
                index = 0
                sell_transaction = 1
                final_difference = 0
                print('Quantity and price at 0th position of the list : {} -> {} '.format(quantities[0], prices[0]))
                while(quantity > 0) :
                    print('Quantity at sell transaction {} is  {}'.format(sell_transaction, quantity))
                    if quantity <=   quantities[index]:
                        print('case --- quantity < quantities[0] ')
                        print('Now the quantity is less than the element of quantity from the list at index 0 : {} < {}'.format(quantity, quantities[0]))
                        cost_price = quantity * prices[index]
                        print('cost price = {} * {}'.format(quantity, prices[index]))
                        sell_price = quantity * price
                        print('sell price = {} * {}'.format(quantity, price))
                        local_difference = sell_price - cost_price
                        final_difference = final_difference + local_difference
                        gains_or_loss_2017 = gains_or_loss_2017 + final_difference
                        actual_quantity_at_0th_position = quantities[index]
                        quantities.remove(quantities[index])
                        quantities.insert(index, (actual_quantity_at_0th_position - quantity))
                        print('New quantity and prices at 0th position of the list - {} {} '.format(quantities[0],
                                                                                                    prices[0]))
                        print('Gain or loss for the quantity {} sold on {} is {} '.format(orig_quantity, row[3], final_difference))
                        quantity = 0
                        print('Calculation completed')
                        print('===============================================================================')
                    elif quantity > quantities[0]:
                        print('case --- quantity > quantities[0] ')
                        print('Calculating gain and loss for sell transaction {} of quantity {} sold at {} on {} '.format(sell_transaction, quantity, price, row[3]))
                        cost_price = quantities[0] * prices[index]
                        print('cost price = {} * {}'.format(quantities[0], prices[index]))
                        sell_price = quantities[0] * price
                        print('sell price = {} * {}'.format(quantities[0], price))
                        local_difference = sell_price - cost_price
                        print('local_difference = {} - {}'.format(sell_price, cost_price))
                        quantity = quantity - quantities[index]
                        print('Available amount from the sell off quantity = {}'.format(quantity))
                        final_difference = final_difference + local_difference
                        quantities.remove(quantities[index])
                        prices.remove(prices[index])
                        print('New quantity and prices at 0th position of the list - {} {} '.format(quantities[0], prices[0]))
                        sell_transaction = sell_transaction + 1
    print('Overall Gain or loss for the year 2017 is {} '.format(gains_or_loss_2017))


if __name__ == '__main__':
    calculate_v2('c:/saurav/self/docs/tax_return/crypto_earnings/gdax/bch.csv')
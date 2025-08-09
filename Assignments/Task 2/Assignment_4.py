print('             No.3 - DICTIONARY                ')

car = {'brand': 'Toyota', 'model': 'Camry', 'year': 2020}
print('Original car:', car)

car['color'] = 'Blue'
print('After adding color:', car)

car['year'] = 2024
print('After updating year:', car)

del car['model']
print('After removing model:', car)

print('             No.2 - DICTIONARY OF PRODUCTS               ')

products = {'apple': 0.50, 'banana': 0.25, 'orange': 0.60}
print('Original prices:', products)

products['apple'] = products['apple'] * 1.10
print('After increasing apple price by 10%:', products)

products['mango'] = 1.25
print('After adding mango:', products)

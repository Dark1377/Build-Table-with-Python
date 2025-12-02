# Dowland libraries "prettytable" and "matplotlib"
from prettytable import PrettyTable
import matplotlib.pyplot as diagram
receipt = PrettyTable()
receipt.field_names=['№','Продукт', 'Цена', 'Количество', 'Стоимость']
product=[]
pay=[]
for i in range(1):
    products=input('Укажите название продукта: ')
    price=int(input('Введите цену продукта: '))
    quantity=int(input('Введите количество продуктов: '))
    receipt.add_row([i+1, products, f'{price} руб.', f'{quantity} шт.', f'{price*quantity} руб.'])
    products.append(products)
    pay.append(price*quantity)
print(receipt)
diagram.bar(products, pay)
diagram.colorbar('green')
diagram.show()

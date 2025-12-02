from prettytable import PrettyTable
import matplotlib.pyplot as diagram
receipt = PrettyTable()
receipt.field_names=['№','Продукт', 'Цена', 'Количество', 'Стоимость']
product=[]
pay=[]
for i in range(1):
    product=input('Укажите название продукта: ')
    price=int(input('Введите цену продукта: '))
    count=int(input('Введите количество продуктов: '))
    receipt.add_row([i+1, product, f'{price} руб.', f'{quantity} шт.', f'{price*quantity}' руб.])
    product.append(product)
    pay.append(price*quantity)
print(receipt)
diagram.bar(product, pay)
diagram.colorbar('green')
diagram.show()

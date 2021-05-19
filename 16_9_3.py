print ('\t Задание 16_9_3')
class Client:
    className = 'Клиент'
    def __init__(self, name, balance):
        self.cl = name
        self.bal = balance
    def __str__(self):
        return f'{self.className},{self.cl}, баланс ={self.bal}'

Client1 = Client('Оливия', 25)
Client2 = Client('Ева', 55)
Client3 = Client('Стюарт', 45)

print (f'{Client1}')
print (f'{Client2}')
print (f'{Client3}')
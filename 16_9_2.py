print ('\t Задание 16_9_2')
class Rectangle:
    def __init__(self, tip, l, w):
        self.tip = tip
        self.a = l
        self.b = w
    def __str__(self):
        return f'{self.tip} = {int(self.a)* int(self.b)}, выс={self.a},' \
               f'шир ={self.b}' # пробелы специально
class Triangle:
    def __init__(self, tip, l1, l2):
        self.tip = tip
        self.a = l1
        self.b = l2

    def __str__(self):
        return f'прямоугольного {self.tip} = {(int(self.a)* int(self.b))/2}, стор1={self.a},' \
               f'стор2 ={self.b}'

Rectangle2 = Triangle('треугольника','15','15')
Rectangle3 = Rectangle('квадрата','14','16')
print (f'Площадь  {Rectangle2}')
print (f'Площадь  {Rectangle3}')
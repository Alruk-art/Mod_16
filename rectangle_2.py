from polimorf import Rectangle, Square, Circle

# далее создаём два прямоугольника

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
# вывод площади наших двух прямков
print (rect_1.get_area_rect())
print (rect_2.get_area_rect())

print ('Площадь квадрата')
sq_1= Square(7)
sq_2 = Square(17)
print(sq_1.get_area_square(),
      sq_2.get_area_square())

print('Площадь круга')
circ_1 = Circle(10)
circ_2 = Circle(20)


figures = [rect_1, rect_2, sq_1, sq_2, circ_1, circ_2]
for figure in figures:
    if isinstance(figure, Square):
        print ('S треуг-к =', figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print('S квадрат=', figure.get_area_rect())
    else:
        print ('S треуг-ка=', figure.get_area())
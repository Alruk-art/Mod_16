
print ( 'Простой вариант без передачи имени из класса в класс')

def id_generator():
    for i in range(1, 9): # лучше больше волонтеров
        yield i
num = id_generator()

class Volunteer:
    def __init__(self, name, city, status):
        self.id = next(num)
        self.city = city
        self.status = status
        self.name = name

    def listout(self):
        return f'{self.id}, {self.name}, г.{self.city}, статус "{self.status}"'

class Student:
    def __init__(self, name, city, status):
        self.id = next(num)
        self.city = city
        self.status = status
        self.name = name

    def listout(self):
        return f'{self.id}, {self.name}, г.{self.city}, должность "{self.status}"'


vol1 = Volunteer("Иван Иванов", "Москва", "Декан")
vol2 = Volunteer("Пётр Петров", "Тула", "профессор")
stud = Student("Иван Петров", "Серпухов", "студент")
print(vol1.listout())
print(vol2.listout())
print(stud.listout())
print()
print ( 'Сложный вариант передаём "имя" из класса в класс')

def id_generator():
    for i in range(1, 9): # лучше больше волонтеров
        yield i

class   Person:
    num1 = id_generator()
    def __init__(self, prsn):
        self.prsn = prsn
        self.num = next(self.num1) # номер в списке

class Volunteer(Person):
    def __init__(self, name, city, status):
        self.city = city
        self.status = status
        Person.__init__(self, name) # имя из class person

    def listout(self):
        return f'{self.num}, {self.prsn}, г.{self.city}, должность "{self.status}"'

class Student(Person):
    def __init__(self, name, city, status):
        self.city = city
        self.status = status
        Person.__init__(self, name) # имя из class person

    def listout(self): # составляем список и возвращаем в печать на экран
        return f'{self.num}, {self.prsn}, г.{self.city}, должность "{self.status}"'

vol1 = Volunteer("Иван Иванов", "Москва", "Декан")
vol2 = Volunteer("Пётр Петров", "Тула", "Профессор")
stud = Student("Иван Петров", "Серпухов", "студент")

print(vol1.listout())
print(vol2.listout())
print(stud.listout())
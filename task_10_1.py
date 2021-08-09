class Employee:
    emp_count = 0
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
        Employee.emp_count += 1
    def setInformation(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
    def getInformation(self):
        return self.__name, self.__age, self.__salary
    def statistik(self):
         if self.__salary > 5000:
             print("Name:", self.__name, "Big boss")
         else:
             print("Name:", self.__name, "Normal")
    def display_count(self):
        print('Всего сотрудников: %d' % Employee.emp_count)
e1=Employee(name='Tom', salary=5500, age=45)
e1.statistik()

class Phone:
    def __init__(self, model, color, num):
        self.__model = model
        self.__color = color
        self.__num = num
    def setInformation2(self, model, color, num):
        self.__model = model
        self.__color= color
        self.__num = num
    def getInformation2(self):
        return self.__model, self.__color, self.__num
    def super_Phone(self):
        if self.__model == 'Nokia':
            print('WoW')
phone1=Phone('Nokia', 'red', '3310')
phone1.super_Phone()

class Song:
    def __init__(self, name, singer, min):
        self.__name = name
        self.__singer = singer
        self.__min = min
    def setInformation(self, name, singer, min):
        self.__name = name
        self.__singer = singer
        self.__min = min
    def getInformation(self):
        return self.__name, self.__singer, self.__min
    def concert(self):
        print('Sing!')







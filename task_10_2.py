class Car:
    def __init__(self, marka, model, year, speed = 0):
        self.__marka = marka
        self.__model = model
        self.__year = year
        self.__speed = speed
    def setInformation(self, marka, model, year, speed):
        self.__marka = marka
        self.__model = model
        self.__year = year
        self.__speed = speed
    def getInformation(self):
        return self.__marka, self.__model, self.__year, self.__speed
    def increse_speed(self):
        return self.__speed + 5
    def decrease_speed(self):
        return self.__speed - 5
    def stop_speed(self):
        return self.__speed - self.__speed
    def display_speed(self):
        return self.__speed
    def reversal_speed(self):
        return self.__speed * (-1)
car1 = Car(marka='Kia', model='Ceed', year=2008, speed=200)


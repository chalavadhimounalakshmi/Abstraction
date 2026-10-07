#1.Food Delivery
from abc import ABC, abstractmethod

class Delivery(ABC):

    @abstractmethod
    def deliver(self):
        pass


class Swiggy(Delivery):

    def deliver(self, distance):
        amount = distance * 20
        print(amount, "Rupees delivery charge through Swiggy")


class Zomato(Delivery):

    def deliver(self, distance):
        amount = distance * 25
        print(amount, "Rupees delivery charge through Zomato")


class Dunzo(Delivery):

    def deliver(self, distance):
        amount = distance * 15
        print(amount, "Rupees delivery charge through Dunzo")


s = Swiggy()
s.deliver(5)

z = Zomato()
z.deliver(5)

d = Dunzo()
d.deliver(5)


print()


#2.calculate Electricity bill
from abc import ABC, abstractmethod

class Electricity(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass


class Home(Electricity):

    def calculate_bill(self, units):
        amount = units * 5
        print(amount, "Rupees home electricity bill")


class Shop(Electricity):

    def calculate_bill(self, units):
        amount = units * 8
        print(amount, "Rupees shop electricity bill")


class Industry(Electricity):

    def calculate_bill(self, units):
        amount = units * 10
        print(amount, "Rupees industry electricity bill")


h = Home()
h.calculate_bill(100)

s = Shop()
s.calculate_bill(100)

i = Industry()
i.calculate_bill(100)
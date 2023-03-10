# -*- coding: utf-8 -*-

#  Pizza Order System - Global AI Hub Akbank Python Bootcamp

import csv
import datetime

with open("Menu.txt", "w") as menu:
    menu.write("""* Lütfen Pizzanızı Seçiniz:
1: Klasik Pizza --> 55₺
2: Margarita -----> 85₺
3: Türk Pizza ----> 60₺
4: Sade Pizza ----> 50₺
5: New York Pizza-> 100₺
6: Kantin Pizza --> 30₺
* Seçmek İstediğiniz Ekstra Malzemeler:
11: Zeytin --> 2.25₺
12: Mantar --> 3.55₺
13: Peynir --> 5.50₺
14: Et ------> 11.50₺
15: Soğan ---> 1.25₺
16: Mısır ---> 3.50₺
17: Mozzarella -> 8.75₺
18: Parmesan  ---> 9.75₺
19: Tulum --> 6.25₺
20: Rokfor ---> 8.25₺
* Seçiminiz İçin Teşekkür Ederiz!\n""")

# Menü seçenekleri için döngü oluşturuyoruz:
with open("Menu.txt") as menu:
    menu_dict = {}
    for line in menu:
        if "*" in line:
            continue
        (key, val) = line.split(": ")
        val = val[:-1]
        menu_dict[int(key)] = val
4


# Üst Pizza sınıfını oluşturalım
class Pizza:
    def get_description(self):  # pizza açıklaması için get metodunu kullandık
        return self.__class__.__name__

    def get_cost(self):  # fiyatı için get metodunu tanımladık
        return self.__class__.cost


# Her bir Pizza için Alt Sınıflarını oluşturalım
class Klasik(Pizza):
    cost = 55.0

    def __init__(self):
        # standart malzemeleri  yazdıralım
        self.description = "Standart Malzemeler: Domates sosu, Zeytin, Biber, Mısır"
        print(self.description + "\n")


class Margarita(Pizza):
    cost = 85.0

    def __init__(self):
        self.description = "Standart Malzemeler: Domates sosu, Mozarella, Zeytin Yağı, Fesleğen"
        print(self.description + "\n")


class TurkPizza(Pizza):
    cost = 60.0

    def __init__(self):
        self.description = "Standart Malzemeler: Domates sosu, Peynir, Sucuk, Biber"
        print(self.description + "\n")


class SadePizza(Pizza):
    cost = 50.0

    def __init__(self):
        self.description = "Standart Malzemeler: Domates sosu, Peynir"
        print(self.description + "\n")


class NewYorkPizza(Pizza):
    cost = 100.0

    def __init__(self):
        self.description = "Standart Malzemeler: Domates sosu, Mısır, Parmesan "
        print(self.description + "\n")


class KantinPizza(Pizza):
    cost = 30.0

    def __init__(self):
        self.description = "Standart Malzemeler: Domates sosu, Zeytin, Biber, Mısır"
        print(self.description + "\n")


# MBurada da malzemeler için üst sınıf oluşturalım. Decorator ile oluşturacağız.
class Decorator(Pizza):
    def __init__(self, topping):
        self.component = topping

    def get_cost(self):
        return self.component.get_cost() + \
            Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
            ' : ' + Pizza.get_description(self)


# Burada malzemeler için alt sınıflar oluşturuyoruz
class Zeytin(Decorator):
    cost = 2.25

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Mantar(Decorator):
    cost = 3.55

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Peynir(Decorator):
    cost = 5.50

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Et(Decorator):
    cost = 11.50

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Sogan(Decorator):
    cost = 1.25

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Misir(Decorator):
    cost = 3.50

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Mozzarella(Decorator):
    cost = 8.75

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Parmesan(Decorator):
    cost = 5.75

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Tulum(Decorator):
    cost = 4.25

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Rokfor(Decorator):
    cost = 0.50

    def __init__(self, topping):
        Decorator.__init__(self, topping)


def main():
    with open("Menu.txt") as cust_menu:
        for l in cust_menu:
            print(l, end="")

    class_dict = {1: Klasik,
                  2: Margarita,
                  3: TurkPizza,
                  4: SadePizza,
                  5: NewYorkPizza,
                  6: KantinPizza,
                  11: Zeytin,
                  12: Mantar,
                  13: Peynir,
                  14: Et,
                  15: Sogan,
                  16: Misir,
                  17: Mozzarella,
                  18: Parmesan,
                  19: Tulum,
                  20: Rokfor}

    code = input("Lütfen Pizzanızı Seçiniz: ")
    while code not in ["1", "2", "3", "4", "5", "6"]:
        code = input("Hatalı Seçim Yaptınız: ")

    order = class_dict[int(code)]()

    while code != "0":
        code = input("Ekstra malzeme numarasını seçiniz (Siparişinizi onaylamak için '0' tuşuna basınız): ")
        if code in ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]:
            order = class_dict[int(code)](order)

    print("\n" + order.get_description().strip() +
          ": ₺" + str(order.get_cost()))
    print("\n")

    print("----------Sipariş Bilgileri----------\n")
    name = input("İsim giriniz: ")
    ID = input("TC kimlik numarası giriniz: ")
    credit_card = input("Kredi kartı numaranısı giriniz: ")
    credit_pass = input("Kredi kartı şifresi giriniz: ")
    time_of_order = datetime.datetime.now()

    with open('Orders_Database.csv', 'a') as orders:
        orders = csv.writer(orders, delimiter=',')
        orders.writerow([name, ID, credit_card, credit_pass, order.get_description(), time_of_order])
    print("Siparişiniz Onaylandı.")


if __name__ == '__main__':
    main()

    
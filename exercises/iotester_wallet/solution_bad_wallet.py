class Wallet:

    def __init__(self, owner_name, balance=0):
        self.__owner_name = owner_name
        self.__balance = balance


    def get_owner_name(self):
        name = self.__owner_name
        self.__owner_name = "oops" # <-- mistake here
        return name


    def get_balance(self):
        return self.__balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False


    def withdraw(self, amount):
        if amount > 0 and self.get_balance() >= amount:
            self.__balance -= amount
            return True
        return False


    def has_more_money(self, other):
        if self.get_balance() > other.get_balance():
            return True
        return False


    def __str__(self):
        return "{:s}: {:.2f} euros".format(self.get_owner_name(), self.get_balance())

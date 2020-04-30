class Employee(object):

    def __init__(self, first_name, last_name, full_name, email, money):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.email = email
        self.money = money

    def __repr__(self):
        return f"Employee({self.first_name}, {self.last_name}, {self.full_name}, {self.email}, {self.money})"

    def __str__(self):
        return f"{self.full_name} - {self.money}"
    
    def new(self, first_name, last_name, full_name, email, money):
        return Employee(first_name, last_name, full_name, email, money)

    @property
    def full_name(self):
        return self.full_name

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

    @property
    def employee_full_name(self):
        return f"{self.full_name}"

    @employee_full_name.setter
    def employee_full_name(self, full_name_string):
        self.full_name = full_name_string.split("-")

    @classmethod
    def from_string(cls, employee_str):
        first_name, last_name, full_name, email, money = employee_str.split("-")
        return cls(first_name, last_name, full_name, email, money)

    
from employee import Employee
from devops_engineer import devops

class manager(Employee):
    """ doc string """

    def __init__(self, first_name, last_name, full_name, email, money, subordinates):
        super().__init__(first_name, last_name, full_name, email, money)
        self.subordinates = subordinates

    def __repr__(self):
        return f"Manager({self.first_name}, {self.last_name}, {self.full_name}, {self.email}, {self.money}, {self.subordinates})"
    
    def __str__(self):
        return f"{self.full_name} - {self.subordinates}"

    def remove_subordinate(self, value):
        if isinstance(value, Employee):
            self.subordinates = self.subordinates.pop(value)
        else:
            for man in self.subordinates:
                if man.email == value:
                    self.subordinates.pop(man)



    def add_subordinate(self, man):
        if isinstance(man, devops):
            self.subordinates = self.subordinates.append(man)
        else:
            raise ValueError("Wrong subordinate type.")

    
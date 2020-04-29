from employee import Employee
from devops_engineer import devops

class manager(Employee):
    """ doc string """

    def __init__(self, first_name, last_name, full_name, email, money, subordinates):
        super().__init__(first_name, last_name, full_name, email, money)
        self.subordinates = (subordinates)

    def add_subordinate(self, man):
        self.subordinates = self.subordinates.append(man)

    def remove_subordinate(self, man):
        self.subordinates = self.subordinates.pop(man)

    
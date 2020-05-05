class Employee(object):

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.full_name = first_name.capitalize() + ', ' + last_name.capitalize()
        self.email = first_name.lower() + '_' + last_name.lower() + '@example.com'
        self.salary = int(salary)

    def __repr__(self):
        return f"Employee({self.first_name}, {self.last_name}, {self.full_name}, {self.email}, {self.salary})"

    def __str__(self):
        return f"{self.full_name} - {self.salary}"

    @property
    def full_name(self):
        return f"{self.first_name.capitalize()}, {self.last_name.capitalize()}"
    
    @full_name.setter
    def full_name(self, full_name_string):
        self.first_name, self.last_name = full_name_string.replace(' ', '').split(",")
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()

    @classmethod
    def from_str(cls, employee_str):
        first_name, last_name, salary = employee_str.split(",")
        return cls(first_name, last_name, int(salary))

class Manager(Employee):
    """ doc string """

    def __init__(self, first_name, last_name, salary, subordinates = []):
        super().__init__(first_name, last_name, salary)
        self.subordinates = subordinates

    def __repr__(self):
        return f"Manager({self.first_name}, {self.last_name}, {self.full_name}, {self.email}, {self.salary}, {self.subordinates})"
    
    def __str__(self):
        return f"{self.full_name} - {self.subordinates}"

    def remove_subordinate(self, value):
        try:
            if isinstance(value, DevOps) and value in self.subordinates:
                self.subordinates.remove(value)
            elif isinstance(value, str):
                for man in self.subordinates:
                    if man.email == value:
                        self.subordinates.remove(man)
        except KeyError:
            pass

    def add_subordinate(self, man):
        if isinstance(man, DevOps):
            self.subordinates.append(man)
        else:
            raise ValueError("Wrong subordinate type.")

class DevOps(Employee):
    """ Doc string """
    def __init__(self, first_name, last_name, salary, skills = []):
        super().__init__(first_name, last_name, salary)
        self.skills = skills
        for s in self.skills: s = s.capitalize()

    def __repr__(self):
        return f"DevOps({self.first_name}, {self.last_name}, {self.full_name}, {self.email}, {self.salary}, {self.skills})"
    
    def __str__(self):
        return f"{self.full_name} - {self.skills}"

    def add_skill(self, skill):
        self.skills.append(skill.capitalize())

    def remove_skill(self, skill):
        self.skills.remove(skill.capitalize())

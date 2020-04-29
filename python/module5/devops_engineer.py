from employee import Employee

class devops(Employee):
    """ Doc string """
    def __init__(self, first_name, last_name, full_name, email, money, skills: list):
        super().__init__(first_name, last_name, full_name, email, money)
        self.skills = skills

    def __repr__(self):
        return f"Devops({self.first_name}, {self.last_name}, {self.full_name}, {self.email}, {self.money}, {self.skills})"
    
    def __str__(self):
        return f"{self.full_name} - {self.skills}"

    def add_skill(self, skill):
        self.skills = self.skills.append(skill)

    def remove_skill(self, skill):
        self.skills = self.skills.pop(skill)
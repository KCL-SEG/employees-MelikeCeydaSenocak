"""Employee pay calculator."""
class Employee:
    def __init__(self, name):
        self.name = name
        self.pay = 0 

    def get_pay(self):
        return self.pay

    def __str__(self):
        return f"{self.name} works and their total pay is {self.pay}."


class SalaryEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.pay = self.monthly_salary

    def get_pay(self):
        return self.pay
    
    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.pay}."


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.pay = self.hourly_wage * self.hours_worked
    
    def get_pay(self):
        return self.pay

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour. Their total pay is {self.pay}."


class CommissionEmployee(SalaryEmployee):
    def __init__(self, name, monthly_salary, commission_rate, contracts_landed):
        super().__init__(name, monthly_salary)
        self.commission_rate = commission_rate
        self.contracts_landed = contracts_landed
        self.pay += (self.commission_rate * self.contracts_landed)
    
    def get_pay(self):
        return self.pay
    
    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour and receives commission for  {self.contracts_landed} at {self.commission_rate}/contract. Their total pay is {self.pay}."
    
class BonusCommissionEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked, bonus_commission):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.bonus_commission = bonus_commission
        self.pay = self.hourly_wage * self.hours_worked + self.bonus_commission
    
    def get_pay(self):
        return self.pay
    
    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.pay}."

        
billie = SalaryEmployee('Billie', 4000)
charlie = HourlyEmployee('Charlie', 25, 100)
renee = CommissionEmployee('Renee', 3000, 200, 4)
jan = CommissionEmployee('Jan', 25 * 150, 220, 3)
robbie = BonusCommissionEmployee('Robbie', 2000, 1500, 500) 
ariel = BonusCommissionEmployee('Ariel', 30, 120, 600) 



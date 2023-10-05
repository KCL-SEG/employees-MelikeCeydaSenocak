"""Employee pay calculator."""
class Employee:
    def __init__(self, name):
        self.name = name
        self.pay = 0  # Initialize pay to zero

    def get_pay(self):
        return self.pay

    def __str__(self):
        return f"{self.name} works and their total pay is {self.pay}."


class SalaryEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.pay = self.monthly_salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary}. Their total pay is {self.pay}."


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.pay = self.hourly_wage * self.hours_worked

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour. Their total pay is {self.pay}."


class CommissionEmployee(SalaryEmployee):
    def __init__(self, name, monthly_salary, commission_rate, contracts_landed):
        super().__init__(name, monthly_salary)
        self.commission_rate = commission_rate
        self.contracts_landed = contracts_landed
        self.pay += self.commission_rate * self.contracts_landed

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a commission for {self.contracts_landed} contract(s) at {self.commission_rate}/contract. Their total pay is {self.pay}."


class BonusCommissionEmployee(SalaryEmployee):
    def __init__(self, name, monthly_salary, bonus_commission):
        super().__init__(name, monthly_salary)
        self.bonus_commission = bonus_commission
        self.pay += self.bonus_commission

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthly_salary} and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.pay}."


# Create the employee objects
billie = SalaryEmployee('Billie', 4000)
charlie = HourlyEmployee('Charlie', 25, 100)
renee = CommissionEmployee('Renee', 3000, 200, 4)
jan = CommissionEmployee('Jan', 25 * 150, 220, 3)
robbie = BonusCommissionEmployee('Robbie', 2000, 1500)
ariel = BonusCommissionEmployee('Ariel', 30 * 120, 600)

# Run tests
print(billie.get_pay())  # Output: 4000
print(str(billie))  # Output: "Billie works on a monthly salary of 4000. Their total pay is 4000."

print(charlie.get_pay())  # Output: 2500
print(str(charlie))  # Output: "Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500."

print(renee.get_pay())  # Output: 3800
print(str(renee))  # Output: "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800."

print(jan.get_pay())  # Output: 4410
print(str(jan))  # Output: "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410."

print(robbie.get_pay())  # Output: 3500
print(str(robbie))  # Output: "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500."

print(ariel.get_pay())  # Output: 4200
print(str(ariel))  # Output: "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200."

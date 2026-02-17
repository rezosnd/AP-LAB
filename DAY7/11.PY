class Employee:
	def __init__(self, name, base_salary):
		self.name = name
		self.base_salary = base_salary


class Salary(Employee):
	def __init__(self, name, base_salary, hra, da):
		super().__init__(name, base_salary)
		self.hra = hra
		self.da = da

	def total_salary(self):
		return self.base_salary + self.hra + self.da


if __name__ == "__main__":
	emp = Salary("Alice", 20000, 5000, 3000)
	print("Total Salary:", emp.total_salary())

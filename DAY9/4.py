class Animal:
	def speak(self):
		print("Animal speaks")

class Dog(Animal):
	def speak(self):
		print("Dog barks")

if __name__ == "__main__":
	a = Animal()
	d = Dog()
	a.speak()
	d.speak()  
# overriding

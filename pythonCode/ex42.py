## Animal is-a object
class Animal(object):
	pass
	
## Dog is-a Animal
class Dog(Animal):
	def __init__(self, name):
		## Dog has-a name of some kind
		self.name = name
		
## Cat is-a Animal
class Cat(Animal):
	def __init__(self, name):
		## Cat has-a name of some kind
		self.name = name
		
## Person is-a object
class Person(object):
	def __init__(self, name):
		## Person has-a name of some kind
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
## Employee is-a Person
class Employee(Person):
	def __init__(self, name, salary):
		super(Employee, self).__init__(name)
		self.salary = salary
		
## Fish is-a object
class Fish(object):
	pass
	
## Salmon is-a Fish
class Salmon(Fish):
	pass
	
## Halibut is-a Fish
class Halibut(Fish):
	pass
	

## rover is-a Dog
rover = Dog("Rover")
print rover.name

## satan is-a Cat
satan = Cat("Satan")
print satan.name

## mary is-a Person
mary = Person("Mary")
## mary has-a pet of some kind
mary.pet = satan

## frank is-a employee
frank = Employee("Frank", 120000)
frank.pet = rover
print frank.name, frank.salary, frank.pet.name

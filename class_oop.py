class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# creting an object 
person1 = Person("Simanga", 30, 'Male')

#invoking the class object
print(person1.name)
print(person1.age)
print(person1.gender)
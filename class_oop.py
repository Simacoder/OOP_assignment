class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    # creating the method object of the person information 
    def introduce(self):
        print(f"Hello, My name is {self.name}. I am {self.age} years old andI am {self.gender}")

# creating the object of the class
person1 = Person("Simanga", 30, "Male")

#invoking the introduce methos o display the Person info
person1.introduce()




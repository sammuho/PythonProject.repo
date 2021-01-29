class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def speak(self):
        print("I am", self.name, "and I am", self.age, "years old")


tim = Dog("Tim", 5)
#tim.age = 7
tim.speak() # This will print "I am Tim and I am 7 years old" 
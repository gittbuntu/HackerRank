class Person:

    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        self.age = 0
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        age = self.age
        if age < 13:
            print("You are young.")
        elif age >= 13 and age < 18:
            print("You are a teenager.")
        elif age >= 18:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        age = 0
        age += 1

    def __str__(self):
        return "you are {} years old".format(self.age)


person = Person(20)
person.amIOld()
person.yearPasses()
print(person)
person.yearPasses()

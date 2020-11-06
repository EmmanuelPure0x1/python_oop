# Creating an animal class as PARENT/BASE/SUPER class.

class Animal:

    def __init__(self): # Initialising the Animal Class
        self.alive = True # creating attributes/variable
        self.spine = True
        self.lungs = True
        self.eyes = True

    # create behaviours as functions /methods
    def breath(self):
        return "Keep breathing to stay alive"

    def move(self):
        return "left to right and up and down..."

    def eat(self):
        return "nom nom nom"

    def procreate(self):
        return "finding partner..."

# Instantiate our class - Create an object
# cat = Animal() #programs looks at all the available behaviours/attributes of the class (self.<attr>)

# cat as child has inherited everything from animal / parent class
# 4 pillars:
# abstracted - eat()
# print(cat.eat())


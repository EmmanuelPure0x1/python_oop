# Python OOP

**Step 1**
- Create an Animal class as our Parent class
```python
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
#print(cat.eat())
```

**Step 2**
- Create reptile class as the child class; so we can ```INHERIT``` from our ```PARENT``` class.
- Abstract 
```python
# This is our first 'Child class' which will inherit from our main 'Animal Class'

# Syntax to import files and classes
from animal import Animal

class Reptile(Animal):

    def __init__(self): # 'Super' key-word is used to inherit everything from a parent class
        super().__init__()
        self.cold_blooded = bool
        self.tetrapod = True
        self.heart_chamber = [3,4]
# we are adding attributes here to make the part of the main animal class accessible the same was but within the reptile class. This is helpful because all of those attr do not need to be added to main class and later need to be turned off if class is later called.

    # creating function for our Reptile class

    def seek_heat(self):
        return "looking for sun shine"

    def hunt(self):
        return "working hard"

    def use_venum(self):
        return "ill use it"

# Lets create object of our reptile class to utilise the amazing functionalities

# reptile_object = Reptile()
# # parent class attr (inherited)
# print(reptile_object.eat())
# print(reptile_object.breath())
# print(reptile_object.procreate())
#
# print("\nThe above are inherited. The below are local attributes\n")
#
# # in this class attr (local)
# print(reptile_object.use_venum())
# print(reptile_object.hunt())
# print(reptile_object.seek_heat())
```
**Step 3**
- Create snake class as child of reptile
```python
# Creating a snake class as a child Class of Reptile

from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True
        self.venom = bool
        self.limbs = False
# creating functions fr our Snake class
    def use_tongue_to_smell(self):
        return "I use my tongue to smell"

snake_obj = Snake()

# Animal class
print(snake_obj.eyes)
print(snake_obj.breath())

print("\n- Above output is inherited from animal class\n")

# Reptile class inherit
print(snake_obj.tetrapod)
print(snake_obj.use_venum())

print("\n- Above output is inherited from reptile class\n")

# Snake (local) class inherit
print(snake_obj.limbs)
print(snake_obj.use_tongue_to_smell())

print("\n- Above output is inherited from local class")

```

**Step 4**
- Create a Python class 
```python
# Creawting python class as child class of our Snake class

from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True

    # creating functions for our python class

    def digest_large_prey(self):
        return "foooooooood"

    def climb(self):
        return "up we go..."

    def squeeze(self):
        return "squeeze to kill!"

    def shed_skin(self):
        return "time to get fresh"

    def hide(self):
        return "waiting for my victim..."

    def swim(self):
        return "swimming across water"

# Initialisation
monty = Python()

# animal class attr
print(monty.eyes)
print(monty.breath())

# reptile class attr
print(monty.tetrapod)
print(monty.seek_heat())

# snake class attr
print(monty.forked_tongue)
print(monty.use_tongue_to_smell())

# python (local) class attr
print(monty.large)
print(monty.swim())
```

- ```__name__``` and ```__main__``` are used to check if the code is run from current file/directly for different file/importing it.
- we will create 2 files and use __name__ and __main__ in both files and the outcome will show the difference
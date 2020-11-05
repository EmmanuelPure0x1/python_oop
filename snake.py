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

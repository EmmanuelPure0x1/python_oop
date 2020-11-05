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
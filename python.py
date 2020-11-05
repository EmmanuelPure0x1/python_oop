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
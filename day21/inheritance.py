class Animal():
    def __init__(slef):
        slef.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(slef):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("underwater!")

    def swim(self):
        print("moving in water")

nemo = Fish()
nemo.breathe()
print(nemo.num_eyes)
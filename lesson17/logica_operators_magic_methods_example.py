


class Horse:
    def __init__(self):
        self.speed = 11
        self.age = 5

    def __add__(self, other):
        if type(other) == Donkey:
            return Mul(self.speed, other.strenght)
        else:
            return Horse()

    def __radd__(self, other):
        return Mul(self.speed, other.strenght)

    def __del__(self):
        print('horse is dead')

    def __iadd__(self, other):
        self.age += other
        return self

    def __bool__(self):
        return False

    def __eq__(self, other):
        return self.speed == other.speed


class Donkey:
    def __init__(self):
        self.strenght = 10
        self.age = 5


class Mul:
    def __init__(self, speed, strenght):
        self.speed = speed
        self.strenght = strenght

    def __add__(self, other):
        return self.strenght + other.strenght

horse = Horse()
donkey = Donkey()
mul = horse + donkey
horse2 = Horse()
horse3 = horse + horse2
mul2 = donkey + horse
print(mul2)
print(mul + mul2)
del horse
print('1')
horse2 += 5
print(bool(horse3))
print(horse2 == horse3)
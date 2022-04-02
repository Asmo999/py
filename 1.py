class Fruit:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __add__(self, other):
        if isinstance(other, Fruit):
            return self.weight + other.weight
        return self.weight

    def __eq__(self, other):
        if isinstance(other, Fruit):
            return self.name == other.name
        return False


banana1 = Fruit("Banana", 0.2)
banana2 = Fruit("Banana", 0.3)
apple = Fruit("Apple", 0.5)
mango = Fruit("Mango", 0.5)

print(f"banana 1 weight: {banana1.weight}")
print(f"banana 2 weight: {banana2.weight}")
print(f"are they the same fruit? {banana1 == banana2}")
print(f"how much do they weigh together? {banana1 + banana2}")
print()
print(f"apple 1 weight: {apple.weight}")
print(f"mango weight: {mango.weight}")
print(f"are they the same fruit? {apple == mango}")
print(f"how much do they weigh together? {apple + mango}")
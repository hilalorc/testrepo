class Robot:
    '''
    This implements a Robot.
    '''
    population = 0

    def __init__(self, name, year):
        self.name = name
        self.year = year
        Robot.population += 1
    def __str__(self):
        my_str = 'My name is' + self.name + 'and my price is' + str(self.price)
        return my_str


    def setEnergy(self, energy):
        self.energy = energy
r1 = Robot("Marvin", 2040)

print(type(r1))

print(r1.__doc__)

print('Robot name:', r1.name)

r1. setEnergy(100)
print(r1.__dict__)
print('Dictionary that stores the attributes:', r1.__dict__)

#print('Energy consumed:', r1.energy)
print('Energy consumed:', getattr(r1, 'energy'))
print(getattr(r1, 'producer', 'Robot without producer'))

r2 = Robot('Calvin', 2030)
r3 = Robot('Gal', 2020)

print(r1)
r1.population += 10
print('Robot population:', Robot.population)
print('Robot population:', r1.population)

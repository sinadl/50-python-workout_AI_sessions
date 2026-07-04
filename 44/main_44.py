class Animal():
    def __init__(self, color, number_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.number_of_legs = number_of_legs
    def __repr__(self):
        return f'{self.color} {self.species},{self.number_of_legs} legs'

class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)
class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)
class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)
class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)
        
        
class cage():
    def __init__(self,id_number):
        self.id_number = id_number
        self.animals = []
    
    def add_animal(self,*animals):
        for animal in animals:
            self.animals.append(animal)
    
    def __repr__(self):
        output = f'cage: {self.id_number}\n'
        output += '\n'.join('\t' + str(animal) for animal in self.animals)
        return output
        
        
wolf = Wolf('black')
sheep = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')
print(wolf)
print(sheep)
print(snake)
print(parrot)

c1 = cage(1)
c1.add_animal(wolf,sheep,snake)
print(c1)
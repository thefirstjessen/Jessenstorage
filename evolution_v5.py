class Human:
    #class atribute
    specie = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name
        self._age = None

    @property
    def intelligent (self):
        raise NotImplementedError('property not implemented')

    @property    
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age must be a positive value")
        self._age = age       

    def of_the_caves(self):
        self.specie = "Homo Neanderthalensis"
        return self    

    @staticmethod
    def species():
        adjectives = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'{adj}' for adj in adjectives)

    @classmethod
    def is_evolved(cls):
        return cls.specie == cls.species()[-1]    


class Neanderthal(Human):
    specie = Human.species()[-2]

    @property
    def intelligent(self):
        return False

class HomoSapiens(Human):
    specie = Human.species()[-1]

    @property
    def intelligent(self):
        return True


if __name__ == '__main__':
    anonymous = Human('Jonh Doe')

    try:
        print(anonymous.intelligent)
    except NotImplementedError:
        print('abstract property')

    jose = HomoSapiens('Jose')
    print('{} of the class {}, intelligent:{}'
    .format(jose.name, jose.__class__.__name__, jose.intelligent))
    grongn = Neanderthal('Grong')
    print('{} of the class {}, intelligent:{}'
    .format(grongn.name, grongn.__class__.__name__, grongn.intelligent))

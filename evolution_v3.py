class Human:
    #atributo de classe
    specie = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name
        self._age = None

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            raise ValueError("Age must to be a positive value")
        self.age = age       

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


class HomoSapiens(Human):
    specie = Human.species()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('Jose')
    jose.set_age(40)
    print(f'Name: {jose.name} Age: {jose.get_age()}')
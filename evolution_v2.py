class Human:
    #atributo de classe
    specie = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name

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
    jose = HomoSapiens('José')
    gronk = Neanderthal('Grokn')
    print(f'Evolution(from class): {",".join(HomoSapiens.species())}')
    print(f'Evolution (from instance): {",".join(jose.species())}')
    print(f'Homo Sapiens evolved? {HomoSapiens.is_evolved()}')
    print(f'Neanderthal evolved?{Neanderthal.is_evolved()}')
    print(f' Jose evolved? {jose.is_evolved()}')
    print(f'Grokn evolved?{gronk.is_evolved()}')
class Human:
    #class atribute
    species = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name

    def of_the_caves(self):
        self.species = "Homo Neanderthalensis"
        return self    


if __name__ == '__main__':
    jose = Human('José')
    gronk = Human('Grokn').of_the_caves()

    print(f'Human.species:{Human.species}')
    print(f'jose.species:{jose.species}')
    print(f'gronkn.species:{gronk.species}')
class Animal:
    @property
    def capabilities(self):
        return ('sleep', 'Eat', 'drink')


class Man(Animal):
    @property
    def capabilities(self):
        return super().capabilities + ('love', 'talk', 'study')


class Spider(Animal):
    @property
    def capabilities(self):
        return super().capabilities +('Make web', 'Walk through walls')


class SpiderMan (Man, Spider):
    @property
    def capabilities(self):
        return super().capabilities + \
            ('beat up bandits', 'shoot webs between buildings')


if __name__ == '__main__':
    jonh = Man()
    print(f'Jonh:{jonh.capabilities}')

    msspider = Spider()
    print(f'donaranha:{msspider.capabilities}')

    peter = SpiderMan()
    print(f'Peter Parker:{peter.capabilities}')

    Lioness = Animal()
    print(f'Lioness :{Lioness .capabilities}')
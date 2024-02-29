class HtmltpStringMixin:
    #HTML convertion
    def __str__(self) -> str:
        html = super().__str__()\
            .replace('(','<string>(')\
            .replace('(', '),</strong>')
        return f'<span>{html}</span>'  


class People:
    def __init__(self, name) -> None:
        self.name = name
              
    def __str__(self):
        return self.name


class Animal:
    def __init__(self, name, pet=True) -> None:
        self.name = name
        self.pet = pet
    
    def __str__(self):
        return self.name + '(pet)' if self.pet else''


class PeopleHtml(HtmltpStringMixin, People):
    pass

class AnimalHtml(HtmltpStringMixin, Animal):
    pass

if __name__ == '__main__':
    p1 = People ('Duda')
    print(p1)

    p2 = PeopleHtml('Roberto Carlos')
    print(p2)

    thor = AnimalHtml('thor')
    print(thor)

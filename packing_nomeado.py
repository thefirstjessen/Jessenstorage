#**kwargs
def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{piloto} -> {posicao}')


if __name__ == '__main__':
    resultado_f1(primeiro ='L.Hamilton',
                 segundo ='M.Verstappen',
                 terceiro='S.Vettel')

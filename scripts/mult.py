#!/usr/bin/env python3
def multiplica(a, b):
    return float(a) * float(b)


def main():
    # a = input('Dona\'m un número: ')
    # b = input('Dona\'m un altre: ')
    # res = multiplica(a, b)
    # print(f'La multiplicació és {res}')
    a = input('Dona\'m un número: ')
    quadrat = multiplica(a, a)
    cub = multiplica(quadrat, a)
    
    print(f'El quadrat de {a} és {quadrat}')
    print(f'El cub de {a} és {cub}')


if __name__ == '__main__':
    main()
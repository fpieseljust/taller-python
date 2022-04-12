#!/usr/bin/env python3
def multiplica(a, b):
    return float(a) * float(b)


def main():
    a = input('Dona\'m un número: ')
    b = input('Dona\'m un altre: ')
    res = multiplica(a, b)
    print(f'La multiplicació és {res}')


if __name__ == '__main__':
    main()
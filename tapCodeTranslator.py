dict = {
    'a': (1, 1), 'b': (1, 2), 'c': (1, 3), 'd': (1, 4), 'e': (1, 5),
    'f': (2, 1), 'g': (2, 2), 'h': (2, 3), 'i': (2, 4), 'j': (2, 5), 'k': (1, 3),
    'l': (3, 1), 'm': (3, 2), 'n': (3, 3), 'o': (3, 4), 'p': (3, 5),
    'q': (4, 1), 'r': (4, 2), 's': (4, 3), 't': (4, 4), 'u': (4, 5),
    'v': (5, 1), 'w': (5, 2), 'x': (5, 3), 'y': (5, 4), 'z': (5, 5),
}


def main(d):
    texto = str(input('Insira o texto para ser convertido: \n')).lower()

    x = ''

    for char in texto:
        if char in d:
            x += str(d[char])
            x += ' '

    print(x + f'\nTexto original: {texto}')


if __name__ == '__main__':
    main(dict)

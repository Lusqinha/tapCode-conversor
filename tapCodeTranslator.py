dict = {
    'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15,
    'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25, 'k': 13,
    'l': 31, 'm': 32, 'n': 33, 'o': 34, 'p': 35,
    'q': 41, 'r': 42, 's': 43, 't': 44, 'u': 45,
    'v': 51, 'w': 52, 'x': 53, 'y': 54, 'z': 55,
}


def main(d):

    while True:
        texto = str(input('Insira o texto para ser convertido: \n')).lower()

        x = ''

        for char in texto:
            if char in d:
                x += str(d[char])
                x += ' '

        print(x + f'\nTexto original: {texto}')

        if input('Deseja continuar? [S/N] ').lower() == 'n':
            break
        else:
            continue


if __name__ == '__main__':
    main(dict)

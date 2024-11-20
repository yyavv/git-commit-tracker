LETTERS = {
    'A': [
        '  A  ',
        ' A A ',
        'AAAAA',
        'A   A',
        'A   A'
    ],
    'B': [
        'BBBB ',
        'B   B',
        'BBBB ',
        'B   B',
        'BBBB '
    ],
    'C': [
        ' CCC ',
        'C   C',
        'C    ',
        'C   C',
        ' CCC '
    ],
    'D': [
        'DDD  ',
        'D  D ',
        'D   D',
        'D  D ',
        'DDD  '
    ],
    'E': [
        'EEEE ',
        'E    ',
        'EEE  ',
        'E    ',
        'EEEE '
    ],
    'F': [
        'FFFFF',
        'F    ',
        'FFF  ',
        'F    ',
        'F    '
    ],
    'G': [
        ' GGG ',
        'G    ',
        'G GGG',
        'G   G',
        ' GGG '
    ],
    'H': [
        'H   H',
        'H   H',
        'HHHHH',
        'H   H',
        'H   H'
    ],
    'I': [
        'IIIII',
        '  I  ',
        '  I  ',
        '  I  ',
        'IIIII'
    ],
    'J': [
        'JJJJJ',
        '   J ',
        '   J ',
        'J  J ',
        ' JJ  '
    ],
    'K': [
        'K   K',
        'K  K ',
        'KK   ',
        'K  K ',
        'K   K'
    ],
    'L': [
        'L    ',
        'L    ',
        'L    ',
        'L    ',
        'LLLLL'
    ],
    'M': [
        'M   M',
        'MM MM',
        'M M M',
        'M   M',
        'M   M'
    ],
    'N': [
        'N   N',
        'NN  N',
        'N N N',
        'N  NN',
        'N   N'
    ],
    'O': [
        ' OOO ',
        'O   O',
        'O   O',
        'O   O',
        ' OOO '
    ],
    'P': [
        'PPPP ',
        'P   P',
        'PPPP ',
        'P    ',
        'P    '
    ],
    'Q': [
        ' QQQ ',
        'Q   Q',
        'Q Q Q',
        'Q  Q ',
        ' QQQQ'
    ],
    'R': [
        'RRRR ',
        'R   R',
        'RRRR ',
        'R  R ',
        'R   R'
    ],
    'S': [
        ' SSS ',
        'S    ',
        ' SSS ',
        '    S',
        ' SSS '
    ],
    'T': [
        'TTTTT',
        '  T  ',
        '  T  ',
        '  T  ',
        '  T  '
    ],
    'U': [
        'U   U',
        'U   U',
        'U   U',
        'U   U',
        ' UUU '
    ],
    'V': [
        'V   V',
        'V   V',
        'V   V',
        ' V V ',
        '  V  '
    ],
    'W': [
        'W   W',
        'W   W',
        'W W W',
        'WW WW',
        'W   W'
    ],
    'X': [
        'X   X',
        ' X X ',
        '  X  ',
        ' X X ',
        'X   X'
    ],
    'Y': [
        'Y   Y',
        ' Y Y ',
        '  Y  ',
        '  Y  ',
        '  Y  '
    ],
    'Z': [
        'ZZZZZ',
        '   Z ',
        '  Z  ',
        ' Z   ',
        'ZZZZZ'
    ],
}

# The following code converts the letters to a binary representation
# where '1' represents a filled space and '0' represents an empty space.
# for letter, data in LETTERS.items():
#     for i, row in enumerate(data):
#         LETTERS[letter][i] = ''.join('1' if char != ' ' else '0' for char in row)

# The following code prints each letter in the LETTERS dictionary in its original form
# and then prints the same letters in a format suitable for inclusion in a dictionary.

# for letter, data in LETTERS.items():
#     print(f"Letter: {letter}")
#     for row in data:
#         print(row)
#     print()  # Add a new line after each letter

# The following code prints each letter in the LETTERS dictionary in a format
# that can be directly copied and pasted into a dictionary definition.
# for letter, data in LETTERS.items():
#     print(f"'{letter}': [")
#     for row in data:
#         print(f"    '{row}',")
#     print("],")


LETTERS_GRID = {   'A': [
    '00100',
    '01010',
    '11111',
    '10001',
    '10001',
],
'B': [
    '11110',
    '10001',
    '11110',
    '10001',
    '11110',
],
'C': [
    '01110',
    '10001',
    '10000',
    '10001',
    '01110',
],
'D': [
    '11100',
    '10010',
    '10001',
    '10010',
    '11100',
],
'E': [
    '11111',
    '10000',
    '11110',
    '10000',
    '11111',
],
'F': [
    '11111',
    '10000',
    '11100',
    '10000',
    '10000',
],
'G': [
    '01110',
    '10000',
    '10111',
    '10001',
    '01110',
],
'H': [
    '10001',
    '10001',
    '11111',
    '10001',
    '10001',
],
'I': [
    '11111',
    '00100',
    '00100',
    '00100',
    '11111',
],
'J': [
    '11111',
    '00010',
    '00010',
    '10010',
    '01100',
],
'K': [
    '10001',
    '10010',
    '11000',
    '10010',
    '10001',
],
'L': [
    '10000',
    '10000',
    '10000',
    '10000',
    '11111',
],
'M': [
    '10001',
    '11011',
    '10101',
    '10001',
    '10001',
],
'N': [
    '10001',
    '11001',
    '10101',
    '10011',
    '10001',
],
'O': [
    '01110',
    '10001',
    '10001',
    '10001',
    '01110',
],
'P': [
    '11110',
    '10001',
    '11110',
    '10000',
    '10000',
],
'Q': [
    '01110',
    '10001',
    '10101',
    '10010',
    '01111',
],
'R': [
    '11110',
    '10001',
    '11110',
    '10010',
    '10001',
],
'S': [
    '01110',
    '10000',
    '01110',
    '00001',
    '01110',
],
'T': [
    '11111',
    '00100',
    '00100',
    '00100',
    '00100',
],
'U': [
    '10001',
    '10001',
    '10001',
    '10001',
    '01110',
],
'V': [
    '10001',
    '10001',
    '10001',
    '01010',
    '00100',
],
'W': [
    '10001',
    '10001',
    '10101',
    '11011',
    '10001',
],
'X': [
    '10001',
    '01010',
    '00100',
    '01010',
    '10001',
],
'Y': [
    '10001',
    '01010',
    '00100',
    '00100',
    '00100',
],
'Z': [
    '11111',
    '00010',
    '00100',
    '01000',
    '11111',
], }
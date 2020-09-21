#!/usr/bin/env python3
"""
Автор: Фамилия Имя


Каждая партия во входном файле описана в отдельной строке.
Порядок клеток следующий:
-------
| 1 | 2 | 3 |
|---+---+---|
| 4 | 5 | 6 |
|---+---+---|
| 7 | 8 | 9 |

Например, партия:
    b,x,x,o,o,o,x,x,o
описывает поле
    |   | x | x |
    |---+---+---|
    | o | o | o |
    |---+---+---|
    | x | x | o |
"""

def read_data(filename='tic-tac-toe-for-public.data'):
    """ читает файл с таблицей партий в крестики-нолики
    :return: список из партий. каждая партия -- список из клеток. слева-направо, сверху вниз
    """ 
    input_file = open(filename)
    data = []
    for line in input_file:
        data+= [ line.strip().split(',') ]
    input_file.close()
    return data



def get_winner(cells):
    """ cells - список значений клеток
    :return: 1 если победил х, иначе 0
    """

    return 1

    

data = read_data()
print(f"загружено {len(data)} партий")

output = open('task1.result.csv','w')

for cells in data:
    winner = get_winner(cells)
    output.write( str(winner)+'\n' )

output.close()
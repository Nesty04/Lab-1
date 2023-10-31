RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
BLACK = '\u001b[30m'
END = '\u001b[0m'

def draw_flag():
  for i in range(6):
    if i == 0 or i == 5:
        print(f'{RED}{"  " * 16}{END}')
    elif i == 1 or i == 4:
        print(f'{WHITE}{"  " * 16}{END}')
    else:
      print(f'{BLUE}{"  " * 16}{END}')

print(draw_flag())


def task_2():
    back_gr = 0
    for i in range(5):
        back_gr += 1
        if i < 2:
            print(f'{WHITE}{"  " * (4 - i)}{RED}{"  " * back_gr}{RED}{"  " * i}{WHITE}{"  " * (9 - (5 + i))}{END}')
        elif i < 3:
            pict = 1
            print(f'{WHITE}{"  " * (4 - i)}{RED}{"  " * (back_gr - 1)}{WHITE}{"  " * pict}{RED}{"  " * i}{WHITE}{"  " * (9 - (5 + i))}{END}')
        elif i < 4:
            pict += 2
            print(f'{WHITE}{"  " * (4 - i)}{RED}{"  " * (back_gr - 2)}{WHITE}{"  " * pict}{RED}{"  " * (i - 1)}{WHITE}{"  " * (9 - (5 + i))}{END}')
        else:
            print(f'{RED}{"  " * 2}{WHITE}{"  " * 5}{RED}{"  " * 2}{END}')

print(task_2())

def task_3():
    plot_list = [[0 for i in range(9)] for i in range(9)]
    result_x = [0.1, 0.2, 0.25, 0.5, 1, 2, 4, 5, 10]
    result_y = [10, 5, 4, 2, 1, 0.5, 0.25, 0.2, 0.1]

    for i in range(9):
        for j in range(9):
            if result_x[i] == 1 / result_y[j]:
                plot_list[i][j] = 1

    for i in range(9):
        line = ''
        for j in range(9):
            if plot_list[i][j] == 0:
                if (i == 3 and j == 2) or (i == 4 and j == 3) or (i == 5 and j == 4):
                    line += '!'
                else:
                    line += '__'
            else:
                if (i == 3 and j == 3) or (i == 4 and j == 4) or (i == 5 and j == 5):
                    line += '!!'
                else:
                    line += '!!!'
        if i <= 5 and i >= 3:
            line += '__'
        print(line)

print(task_3())


def task_4():
    with open('sequence.txt') as fh:
        result = []
        for num_str in fh:
            num = float(num_str)
            if num > 0:
                if num != 5:
                    result.append(num)
        return result
    

if __name__ == '__main__':
    print(task_4())

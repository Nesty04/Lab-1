RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

# def draw_flag():
#   for i in range(6):
#     if i == 0 or i == 5:
#         print(f'{RED}{"  " * 16}{END}')
#     elif i == 1 or i == 4:
#         print(f'{WHITE}{"  " * 16}{END}')
#     else:
#       print(f'{BLUE}{"  " * 16}{END}')

# print(draw_flag())


# plot_list = [[0 for i in range(10)] for i in range(10)]
# result = [0 for i in range(10)]

# for i in range(10):
#     result[i] = i ** 3

# step = round(abs(result[0] - result[9]) / 9, 2)
# print(step)

# for i in range(10):
#     for j in range(10):
#         if j == 0:
#             plot_list[i][j] = step * (8-i) + step

# for i in range(9):
#     for j in range(10):
#         if abs(plot_list[i][0] - result[9 - j]) < step:
#             for k in range(9):
#                 if 8 - k == j:
#                     plot_list[i][k+1] = 1

# for i in range(9):
#     line = ''
#     for j in range(10):
#         if j == 0:
#             line += '\t' + str(int(plot_list[i][j])) + '\t'
#         if plot_list[i][j] == 0:
#             line += '--'
#         if plot_list[i][j] == 1:
#             line += '!!'
#     print(line)
# print('\t0\t1 2 3 4 5 6 7 8 9')

# for i in range(10):
#     #print(plot_list[i])
#     pass

# def task_4():
#     with open('sequence.txt') as fh:
#         result = []
#         for num_str in fh:
#             num = float(num_str)
#             if num > 0:
#                 if num != float(5):
#                     result.append(num)
#         return result
    

# if __name__ == '__main__':
#     print(task_4())
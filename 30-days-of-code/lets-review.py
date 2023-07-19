if __name__ == '__main__':
    N = int(input())
    input_list = []

    even_list = []
    odd_list = []

    for i in range(N):
        input_list.append(input())
        even_list.append('')
        odd_list.append('')

        for j in range(len(input_list[i])):
            if j % 2 == 0:
                even_list[i] += input_list[i][j]
            else:
                odd_list[i] += input_list[i][j]

    for k in range(len(even_list)):
        print(f'{even_list[k]} {odd_list[k]}')

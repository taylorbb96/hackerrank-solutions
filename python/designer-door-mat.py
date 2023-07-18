if __name__ == '__main__':
    dimensions = input().split()
    N = int(dimensions[0])
    M = int(dimensions[1])

    middle_width = 1

    for i in range(N // 2):
        side_width = (M - middle_width*3) // 2
        print('-'*side_width + '.|.'*middle_width + '-'*side_width)

        middle_width += 2

    print(('-'*(M//2-3)) + 'WELCOME' + ('-'*(M//2-3)))

    middle_width -= 2

    for i in range(N // 2):
        side_width = (M - middle_width*3) // 2
        print('-'*side_width + '.|.'*middle_width + '-'*side_width)

        middle_width -= 2

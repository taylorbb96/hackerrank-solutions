if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    integer_list = list(integer_list)

    t = ()
    for i in range(n):
        t += (integer_list[i],)

    print(hash(t))

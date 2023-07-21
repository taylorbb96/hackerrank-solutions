if __name__ == '__main__':
    n = int(input())
    phonebook = {}

    for i in range(n):
        name_and_number = input().split()
        phonebook[name_and_number[0]] = name_and_number[1]

    while True:
        try:
            query_name = input()
            if query_name in phonebook:
                print(f'{query_name}={phonebook[query_name]}')
            else:
                print('Not found')
        except:
            break

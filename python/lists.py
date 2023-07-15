if __name__ == '__main__':
    N = int(input())

    result = []

for i in range(N):
    command = input().split()
    match command[0]:
        case 'append':
            result.append(command[1])
        case 'insert':
            result.insert(int(command[1]), command[2])
        case 'print':
            print(result)
        case 'remove':
            result.remove(command[1])
        case 'sort':
            result.sort()
        case 'pop':
            result.pop()
        case 'reverse':
            result.reverse()

# This actually doesn't work for the challenge, but it annoys me that the version of Python on HackerRank doesn't have match case so I'm putting it here anyway

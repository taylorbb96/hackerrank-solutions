if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = list(arr)
    max_score = max(arr)
    highest_so_far = min(arr)

    for i in arr:
        if i == max_score:
            continue
        if i > highest_so_far:
            highest_so_far = i

    print(highest_so_far)

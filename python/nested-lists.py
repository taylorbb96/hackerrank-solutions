if __name__ == '__main__':
    records = []
    scores = []
    for i in range(int(input())):
        name = input()
        score = float(input())

        records.append([name, score])
        scores.append(score)

    lowest = min(scores)
    second_lowest = max(scores)

    for j in range(len(records)):
        if records[j][1] == lowest:
            continue
        if records[j][1] < second_lowest:
            second_lowest = records[j][1]

    result = []

    for k in range(len(records)):
        if records[k][1] == second_lowest:
            result.append(records[k][0])

    result.sort()

    for l in result:
        print(l)

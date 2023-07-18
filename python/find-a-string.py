def count_substring(string, sub_string):
    count = 0
    remaining_string = string
    while True:
        if remaining_string.find(sub_string) == -1:
            break

        count += 1
        remaining_string = remaining_string[remaining_string.find(
            sub_string)+1:]
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

def swap_case(s):
    s_out = ''
    for i in s:
        if i.islower():
            s_out += i.upper()
        else:
            s_out += i.lower()
    return s_out


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

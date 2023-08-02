import string

def print_rangoli(size):
    total_width = (size*2)-1 + (size-1)*2

    alphabet = list(string.ascii_lowercase)

    for x in range(size-1, -1, -1):
        pattern = []
        for y in range(x,size):
            pattern.append(alphabet[y])
        for z in range(x+1,size):
            pattern.insert(0,alphabet[z])
        s = "-".join(pattern)
        print(s.center(total_width,"-"))

    for x in range(1, size, 1):
        pattern = []
        for y in range(x,size):
            pattern.append(alphabet[y])
        for z in range(x+1,size):
            pattern.insert(0,alphabet[z])
        s = "-".join(pattern)
        print(s.center(total_width,"-"))
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
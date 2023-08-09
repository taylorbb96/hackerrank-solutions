def merge_the_tools(string, k):
    subsequences = [string[i:i+k] for i in range(0,len(string),k)]

    for subsequence in subsequences:
        output = ''

        for char in subsequence:
            if char not in output:
                output += char

        print(output)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
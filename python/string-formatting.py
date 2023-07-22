def print_formatted(number):
    max_width = len(bin(number)[2:])

    for i in range(1, number+1):
        oct_i = oct(i)[2:]
        hex_i_lower = hex(i)[2:]
        hex_i = ''
        for char in hex_i_lower:
            hex_i += char.capitalize()
        bin_i = bin(i)[2:]

        print(
            f"{i:>{max_width}} {oct_i:>{max_width}} {hex_i:>{max_width}} {bin_i:>{max_width}}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

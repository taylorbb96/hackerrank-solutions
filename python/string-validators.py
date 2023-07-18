if __name__ == '__main__':
    s = input()

    has_alphanumeric = False
    has_alphabetical = False
    has_digit = False
    has_lowercase = False
    has_uppercase = False

    for i in s:
        if i.isalnum():
            if i.isdigit():
                has_alphanumeric = True
                has_digit = True
                continue
            if i.isalpha():
                if i.islower():
                    has_lowercase = True
                    has_alphanumeric = True
                    has_alphabetical = True
                    continue
                if i.isupper():
                    has_uppercase = True
                    has_alphanumeric = True
                    has_alphabetical = True
                    continue

    print(has_alphanumeric)
    print(has_alphabetical)
    print(has_digit)
    print(has_lowercase)
    print(has_uppercase)

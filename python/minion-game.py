def minion_game(string):
    vowels = ['A','E','I','O','U']
    
    kevin_score = 0
    stuart_score = 0
    
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i
            
    
    if stuart_score > kevin_score:
        string_out = f'Stuart {stuart_score}'
    elif kevin_score > stuart_score:
        string_out = f'Kevin {kevin_score}'
    else:
        string_out = 'Draw'
        
    print(string_out)
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
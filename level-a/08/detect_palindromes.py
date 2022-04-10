import math

def is_palindrome(word):
    j = len(word)-1
    result = 0
    for i in range(len(word)):
        if word[i] == word[j]:
            result = result + 1
        if i >= j:
            break
        j = j - 1
    
    if result == math.ceil(len(word)/2):
        return True
    else:
        return False

def is_palindrome_recursive(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome_recursive(word[1:-1])


words = ["arara", "racecar", "carro", "cama", "level"]

for word in words:
    print(word)
    print(is_palindrome_recursive(word))
    print("\n")
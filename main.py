def is_palindrome(string):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    new_string = []

    for letter in string:
        if letter in alphabet:
            new_string.append(letter.lower())

    reversed_string = new_string[:]
    
    left_pointer = 0
    right_pointer = len(reversed_string) - 1

    while left_pointer < right_pointer:
        temp = reversed_string[left_pointer]
        reversed_string[left_pointer] = reversed_string[right_pointer]
        reversed_string[right_pointer] = temp
        left_pointer += 1
        right_pointer -= 1

    return new_string == reversed_string

print(is_palindrome("level"))

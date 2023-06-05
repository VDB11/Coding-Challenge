'''2) Write a Python function named letter_frequency_counter that takes a 
string as input and returns a dictionary. The dictionary should have each unique letter in the string as a 
key and the frequency of that letter as the corresponding value. The function should ignore spaces and be 
case-insensitive.'''


def letter_frequency_counter(string):
    freq = {}
    for char in string.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq

str1 = "Hello World"
print(letter_frequency_counter(str1))


str2 = "Python programming"
print(letter_frequency_counter(str2))



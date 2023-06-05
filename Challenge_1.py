''' 1) Write a Python function that takes two strings as input and find the longest substring that is 
common to both strings.'''

def lcs(string1, string2):
    longest_length = 0
    ending_index = 0
    table = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]

    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            if string1[i - 1] == string2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > longest_length:
                    longest_length = table[i][j]
                    ending_index = i
    longest_substring = string1[ending_index - longest_length:ending_index]

    return longest_substring

str1 = "foobarbaz"
str2 = "barfoobaz"
result = lcs(str1, str2)
print(result)

str3 = 'abcdefg'
str4 = 'xyabcz'
result = lcs(str3, str4)
print(result)







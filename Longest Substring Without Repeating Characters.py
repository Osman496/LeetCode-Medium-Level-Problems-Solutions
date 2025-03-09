# 1. Step by Step Explanation of the Code
# This code is designed to find the length of the longest substring without repeating characters in a given string s. Here's how it works step by step:

# Initialization:

# start: This variable keeps track of the starting index of the current substring without repeating characters.

# max_len: This variable stores the length of the longest substring found so far.

# used_char: This is a dictionary that keeps track of the last seen index of each character in the string.

# Iteration:

# The code iterates through each character in the string s using a for loop.

# For each character s[i], it checks if the character has already been seen (i.e., it exists in used_char) and if the last seen index of the character is within the current substring (i.e., start <= used_char[s[i]]).

# If the character is repeated within the current substring, the start index is updated to the next index of the previously seen character (used_char[s[i]] + 1).

# Update:

# The used_char dictionary is updated with the current character and its index.

# The length of the current substring (i - start + 1) is calculated and compared with max_len. If it's longer, max_len is updated.

# Return:

# After the loop finishes, the function returns max_len, which is the length of the longest substring without repeating characters.


def longest_substring(s):
    start = 0  # Initialize the starting index of the current substring
    max_len = 0  # Initialize the maximum length of the substring found so far
    used_char = {}  # Dictionary to store the last seen index of each character

    for i in range(len(s)):  # Iterate through each character in the string
        if s[i] in used_char and start <= used_char[s[i]]:
            # If the character is repeated and its last seen index is within the current substring
            start = used_char[s[i]] + 1  # Move the start index to the next character
        used_char[s[i]] = i  # Update the last seen index of the current character
        max_len = max(max_len, i - start + 1)  # Update the maximum length if the current substring is longer

    return max_len  # Return the length of the longest substring without repeating characters

# Example usage
print(longest_substring("abcabdfbcde"))  # Output: 5


# 3. Final Explanation
# Example Walkthrough:
# For the input string "abcabdfbcde":

# The function starts with start = 0 and max_len = 0.

# It iterates through the string:

# At i = 0, character 'a' is added to used_char with index 0. The current substring length is 1, so max_len becomes 1.

# At i = 1, character 'b' is added to used_char with index 1. The current substring length is 2, so max_len becomes 2.

# At i = 2, character 'c' is added to used_char with index 2. The current substring length is 3, so max_len becomes 3.

# At i = 3, character 'a' is repeated. The start index is updated to 1 (the next index after the previous 'a'). The current substring length is 3, so max_len remains 3.

# At i = 4, character 'b' is repeated. The start index is updated to 2 (the next index after the previous 'b'). The current substring length is 3, so max_len remains 3.

# At i = 5, character 'd' is added to used_char with index 5. The current substring length is 4, so max_len becomes 4.

# At i = 6, character 'f' is added to used_char with index 6. The current substring length is 5, so max_len becomes 5.

# At i = 7, character 'b' is repeated. The start index is updated to 3 (the next index after the previous 'b'). The current substring length is 5, so max_len remains 5.

# At i = 8, character 'c' is repeated. The start index is updated to 4 (the next index after the previous 'c'). The current substring length is 5, so max_len remains 5.

# At i = 9, character 'd' is repeated. The start index is updated to 6 (the next index after the previous 'd'). The current substring length is 4, so max_len remains 5.

# At i = 10, character 'e' is added to used_char with index 10. The current substring length is 5, so max_len remains 5.

# The function returns 5, which is the length of the longest substring without repeating characters ("cabdf" or "abdfb").

# Key Points:
# The algorithm efficiently finds the longest substring without repeating characters in O(n) time, where n is the length of the string.

# It uses a sliding window approach with two pointers (start and i) and a dictionary to track character indices.
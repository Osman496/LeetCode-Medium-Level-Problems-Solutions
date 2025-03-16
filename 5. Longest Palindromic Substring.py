
# Explanation
# Your solution uses the "expand around center" approach to find the longest palindromic substring. It iterates through the string, treating each character (and each pair of characters) as the center of a potential palindrome. It then expands outward to find the longest palindrome and keeps track of the longest one found.

# Approach
# Initialize Variables:

# Use p to store the longest palindrome found.

# Use p_len to store the length of the longest palindrome.

# Expand Around Center:

# For each character, treat it as the center of an odd-length palindrome and expand outward.

# For each pair of characters, treat them as the center of an even-length palindrome and expand outward.

# Update the Longest Palindrome:

# If a longer palindrome is found, update p and p_len.

# Return the Result:

# After iterating through the string, return the longest palindrome found


class Solution(object):
    def longestPalindrome(self, s):
        # Initialize variables to store the longest palindrome and its length
        p = ""
        p_len = 0

        # Iterate through the string
        for i in range(len(s)):
            # Case 1: Odd-length palindrome (center is a single character)
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # If the current palindrome is longer, update p and p_len
                if (right - left + 1) > p_len:
                    p = s[left:right + 1]
                    p_len = right - left + 1
                # Expand outward
                left -= 1
                right += 1

            # Case 2: Even-length palindrome (center is a pair of characters)
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # If the current palindrome is longer, update p and p_len
                if (right - left + 1) > p_len:
                    p = s[left:right + 1]
                    p_len = right - left + 1
                # Expand outward
                left -= 1
                right += 1

        # Return the longest palindromic substring
        return p
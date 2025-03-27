# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

# The algorithm for myAtoi(string s) is as follows:

# Whitespace: Ignore any leading whitespace (" ").
# Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
# Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
# Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
# Return the integer as the final result.

# Problem Explanation
# The task is to implement the myAtoi(string s) function, which converts a string into a 32-bit signed integer following these rules:

# Ignore leading whitespaces (" ") until a non-space character is found.

# Check for a sign (+ or -) and determine if the number is positive or negative.

# Extract digits and form the number until a non-digit character appears.

# Handle integer overflow:

# If the number exceeds 2^31 - 1 (2147483647), return 2147483647.

# If the number goes below -2^31 (-2147483648), return -2147483648.

# Return the final integer after applying the sign.

# 1️⃣ Initialize Variables
# Use i = 0 to traverse the string.

# Store sign = 1 (assume positive by default).

# Use result = 0 to build the number.

# Define max_int = 2^31 - 1 and min_int = -2^31 for overflow handling.

# 2️⃣ Skip Leading Whitespaces
# Use a while loop to move i forward until the first non-space character is found.

# 3️⃣ Check for Sign (+ or -)
# If the character is '-', set sign = -1.

# If the character is '+', keep sign = 1.

# Move i forward.

# 4️⃣ Convert Digits to Integer
# Run a while loop as long as s[i] is a digit (0-9).
# If result exceeds max_int, return the clamped value (max_int or min_int).

# 5️⃣ Apply the Sign and Return the Result
# Finally, multiply result by sign and return the value.

# Time Complexity Analysis
# Skipping spaces → O(N), but only runs for leading spaces.

# Reading digits → O(N), where N is the length of numeric part.

# Overall Complexity → O(N), since we process each character once.

def StrToInt(s):
    i = 0 #Point of traverse for string
    len_s = len(s) #Length of String
    sign = 1 #Sign of number
    result = 0 #To Store end result
    max_int = 2**31 - 1 #For checking maximum range
    min_int = -2**31 #For checking minimum range
    while i < len_s and s[i] == " ": #To check any leading whitespace
        i += 1 #Move to next character
    if i < len_s and s[i] == "-": #To check for -ive sign
        sign = -1
        i += 1 #Move to next character
    elif i < len_s and s[i] == "+": #To check for +ive sign
        i += 1 #Move to next character
    while i < len_s and s[i].isdigit(): #To check for digit
        result = result * 10 + int(s[i])
        while result > max_int: #To check for maximum range
            return max_int if sign == 1 else min_int
        i += 1
    return result * sign

print(StrToInt("42"))
print(StrToInt("   -42"))
print(StrToInt("4193 with words"))
print(StrToInt("words and 987"))
print(StrToInt("-91283472332"))

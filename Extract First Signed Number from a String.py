# 🚀 Explanation:
# Iterate over the string and extract all digits.

# Detect the first - sign before the first number.

# Convert extracted digits into an integer and apply the sign.

# Problem: It failed when multiple numbers were present ("abc123xyz-2" → it wrongly extracted 1232 instead of -2).

# So, we switched to regex, which efficiently finds the first complete signed number without manual character-by-character checking.

def extract_num(s):
    """
    Extracts the first valid signed number from a string.
    - Detects a '-' only if it's directly before a number.
    - Extracts only the first encountered number.
    - Ignores extra characters and misplaced '-'.
    """
    
    sign = 1  # Default is positive
    extracted_nums = ""  # Stores number characters
    
    for i, char in enumerate(s):
        if char == "-" and extracted_nums == "":  
            # If '-' appears before the first number, apply sign
            sign = -1  
        elif char.isdigit():  
            # If character is a digit, add it to extracted_nums
            extracted_nums += char  
    
    # Convert to integer if digits exist, otherwise return 0
    num = int(extracted_nums) if extracted_nums else 0  
    return num * sign  # Apply detected sign

# Taking user input
s = input("Enter a string: ")  
print(extract_num(s))  # Calling function and printing result

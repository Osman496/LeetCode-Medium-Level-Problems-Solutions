# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


# Solution 1:

# Explanation
# The provided function maximumSubaray calculates the maximum sum of a contiguous subarray within the given array nums. It uses a modified version of Kadane's Algorithm, which is an efficient way to solve this problem in O(n) time complexity with O(1) space complexity.

# The key idea is to iterate through the array while maintaining two variables:

# currentSubArr: Tracks the sum of the current subarray being considered.

# maxSubArr: Stores the maximum sum found so far.

# At each step, the algorithm decides whether to continue the current subarray or start a new subarray from the current element. If the sum of the current subarray becomes negative, it resets currentSubArr to 0, effectively starting a new subarray from the next element. This ensures that the algorithm always considers the maximum possible subarray sum.

# Approach
# Initialization:

# Set maxSubArr to the first element of the array, as this is the initial maximum sum.

# Set currentSubArr to 0, as it will accumulate the sum of the current subarray.

# Iteration:

# For each element n in the array:

# If currentSubArr is negative, reset it to 0. This ensures that we don't carry forward a negative sum, as starting a new subarray from the current element would yield a better result.

# Add the current element n to currentSubArr.

# Update maxSubArr to be the maximum of maxSubArr and currentSubArr.

# Result:

# After iterating through the array, maxSubArr will contain the maximum sum of any contiguous subarray.

def maximumSubaray(nums):
    # Initialize maxSubArr with the first element of the array
    maxSubArr = nums[0]
    # Initialize currentSubArr to 0
    currentSubArr = 0
    
    # Iterate through each element in the array
    for n in nums:
        # If currentSubArr is negative, reset it to 0
        # This ensures we don't carry forward a negative sum
        if currentSubArr < 0:
            currentSubArr = 0
        # Add the current element to currentSubArr
        currentSubArr += n
        # Update maxSubArr to be the maximum of itself and currentSubArr
        maxSubArr = max(maxSubArr, currentSubArr)
    
    # Return the maximum subarray sum found
    return maxSubArr

# Example usage
print(maximumSubaray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6



# Solution 2:

# Explanation
# Initialization: current_max and max_so_far are initialized to the first element to handle cases where all elements are negative.

# Iteration: For each subsequent element, current_max is updated to either start a new subarray at the current element or extend the previous subarray. This ensures we always consider the best possible subarray ending at the current position.

# Updating Maximum: max_so_far is updated each iteration to ensure we track the highest sum encountered, which gives the final result.
# Approach:

# Initialization: Start by initializing two variables, current_max and max_so_far, both set to the value of the first element in the array. These variables track the maximum sum ending at the current position and the overall maximum sum found so far, respectively.

# Iteration: Traverse the array starting from the second element. For each element, update current_max to be the maximum of the current element itself or the sum of current_max and the current element. This step decides whether to start a new subarray at the current element or continue the existing subarray.

# Update Maximum: Update max_so_far to keep track of the highest sum encountered during the iteration.

# Result: After processing all elements, max_so_far holds the maximum subarray sum.
def maxSubArray(nums):
    if not nums:
        return 0  # Assuming the problem states nums is non-empty, this line can be omitted
    current_max = max_so_far = nums[0]
    for num in nums[1:]:
        current_max = max(num, current_max + num)
        max_so_far = max(max_so_far, current_max)
    return max_so_far

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to simplify the code
        dummy = ListNode(0)
        # Use a pointer to build the result linked list
        current = dummy
        carry = 0

        # Traverse both linked lists
        while l1 or l2 or carry:
            # Get the values of the current nodes (or 0 if the list is exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10

            # Create a new node with the digit value and move the pointer
            current.next = ListNode(total % 10)
            current = current.next

            # Move to the next nodes in the input lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Return the result linked list (skip the dummy node)
        return dummy.next
    
# Explanation:

# Dummy Node:

# A dummy node is created to simplify the process of building the result linked list. It acts as a placeholder for the head of the result list.

# Pointer (current):

# A pointer (current) is used to traverse and build the result linked list.

# Carry:

# A carry variable is used to keep track of the carry-over when the sum of two digits is 10 or more.

# Traversal:

# The while loop continues until both input lists (l1 and l2) are exhausted and there is no carry left.

# Sum Calculation:

# For each iteration, the values of the current nodes from l1 and l2 are added along with the carry.

# The sum is used to calculate the new digit (total % 10) and the new carry (total // 10).

# New Node Creation:

# A new node is created with the digit value and appended to the result linked list.

# Move to Next Nodes:

# The pointers for l1 and l2 are moved to the next nodes if they exist.

# Return Result:

# The result linked list starts from the next node of the dummy node, so dummy.next is returned.
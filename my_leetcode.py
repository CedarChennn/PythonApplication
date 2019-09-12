def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """

    # The stack to keep track of opening brackets.
    stack = []

    # Hash map for keeping track of mappings. This keeps the code very clean.
    # Also makes adding more types of parenthesis easier
    mapping = {")": "(", "}": "{", "]": "["}

    # For every bracket in the expression.
    for char in s:

        # If the character is an closing bracket
        if char in mapping:

            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy value of '#' to the top_element variable
            top_element = stack.pop() if stack else '#'

            # The mapping for the opening bracket in our hash and the top
            # element of the stack don't match, return False
            if mapping[char] != top_element:
                return False
        else:
            # We have an opening bracket, simply push it onto the stack.
            stack.append(char)

    # In the end, if the stack is empty, then we have a valid expression.
    # The stack won't be empty for cases like ((()
    return not stack
def threeSum(self, nums: [int]) -> [[int]]:
    nums.sort()
    res, k = [], 0
    for k in range(len(nums) - 2):
        if nums[k] > 0: break # 1. because of j > i > k.
        if k > 0 and nums[k] == nums[k - 1]: continue # 2. skip the same `nums[k]`.
        i, j = k + 1, len(nums) - 1
        while i < j: # 3. double pointer
            s = nums[k] + nums[i] + nums[j]
            if s < 0:
                i += 1
                while i < j and nums[i] == nums[i - 1]: i += 1
            elif s > 0:
                j -= 1
                while i < j and nums[j] == nums[j + 1]: j -= 1
            else:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]: i += 1
                while i < j and nums[j] == nums[j + 1]: j -= 1
        return res
def cloneGraph_133(self, node: 'Node') -> 'Node':
#
#definition for a node.
#class node:
#    def __init__(self, val, neighbors):
#        self.val = val
#        self.neighbors = neighbors
#
        lookup = {}
        def dfs(node):
            #print(node.val)
            if not node: return
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, [])
            lookup[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            
            return clone

        return dfs(node)
def evalRPN_150(self, tokens: List[str]) -> int:
    stack = []
    for i in tokens:
        if i in ["+", "-", "*", "/"]:
            a,b = stack.pop(),stack.pop()
            stack.append(str(int(eval(b + i + a))))
        else:
            stack.append(i)
    return stack[-1]

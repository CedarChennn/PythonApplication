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

def findTargetSumWays(self, nums: List[int], S: int) -> int:   #unknow
        d = {}
        def dfs(i, cur, d):
            if i < len(nums) and (i, cur) not in d: # 搜索周围节点
                d[(i, cur)] = dfs(i + 1, cur + nums[i], d) + dfs(i + 1, cur - nums[i], d)
            return d.get((i, cur), int(cur == S))   
        return dfs(0, 0, d)


def lengthOfLongestSubstring(self, s: str) -> int:
    if not s:return 0
    n = len(s)
    cur_len = 0
    max_len=0
    left=0
    lookup=set()
    for i in range(n):
        cur_len+=1
        while(s[i] in lookup):
            lookup.remove(s[left])
            left+=1
            cur_len-=1
        if(cur_len>max_len):
            max_len=cur_len
        lookup.add(s[i])
    return max_len

def topKFrequent(nums,k):
    dic={}
    for i in nums:
        dic[i]=dic.get(i,0)+1
    res=[]
    for i in sorted(dic.items(),key =lambda dic:dic[1],reverse=True):
        k=k-1
        res.append(i[0])
        if(k==0):
            break
    return res


def search(nums,target):
    end=len(nums)-1
    start=0
    while(start<end-1):
        mid=start+(end-start)//2
        if(nums[mid]==target):
            return mid
        if(nums[mid]>target):
            end=mid
        if(nums[mid]<target):
            start=mid
    if(nums[start]==target):
        return start
    if(nums[end]==target):
        return end
    return -1


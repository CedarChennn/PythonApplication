def cloneGraph(self, node: 'Node') -> 'Node':
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

def numJewelsInStones( J, S):
    d={}
    for i in J:
        d[i]=0
    for i in S:
        if i in d.keys():
            d[i]+=1
        
    res=0
    for i in d.values():
        res+=i
        print(res)
    return i




def main():
    print(numJewelsInStones("aA","aAAbbbb"))




if __name__ == "__main__":
    main()
    
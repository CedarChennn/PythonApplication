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






if __name__ == "__main__":
    print("hello")
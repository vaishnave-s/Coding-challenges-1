class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hashmap =set()
        for n1,n2 in edges:
            if n1 not in hashmap:
                hashmap.add(n1)
            else:
                return n1
            if n2 not in hashmap:
                hashmap.add(n2)
            else:
                return n2
                

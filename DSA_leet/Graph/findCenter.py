class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hashmap = {}
        for n1,n2 in edges:
            if n1 not in hashmap:
                hashmap[n1]=1
            else:
                hashmap[n1]+=1
            if n2 not in hashmap:
                hashmap[n2]=1
            else:
                hashmap[n2]+=1
        for k,v in hashmap.items():
            if v!=1:
                return k

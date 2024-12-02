class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i,val in enumerate(sentence.split(" ")):
            if searchWord in val:
                if val[:len(searchWord)] == searchWord:
                    return i+1
        return -1

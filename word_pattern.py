class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word=s.split(" ")
        if len(pattern)!=len(word):
            return False
        else:
            return len(set(word))==len(set(pattern))==len(set(zip(pattern,word)))

        

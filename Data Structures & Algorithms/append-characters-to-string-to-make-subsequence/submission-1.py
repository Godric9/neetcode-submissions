class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(t)
        counter = 0
        for c in s:
            if c == t[counter]:
                counter+=1
            if counter == n:
                return 0
        
        return n - counter
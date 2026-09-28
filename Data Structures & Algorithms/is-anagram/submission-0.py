class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False
        one = {}
        for c in s:
            if c in one:
                one[c] += 1
            else:
                one[c] = 1
        two = {}
        for c in t:
            if c in two:
                two[c] += 1
            else:
                two[c] = 1
        return one == two

        
        
            
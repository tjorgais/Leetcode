from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        func=Counter(s)
        for l in t:
            if l in func and func[l]!=0:
                func[l]-=1
            else:
                return False
        return True
        
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        func1=Counter(s)
        func2=Counter(t)
        if func1==func2:
            return True
        else:
            return False
        
        
        ##using dictionary O(n)
        
        
        # if len(s)!=len(t):
        #     return False
        # func=Counter(s)
        # for l in t:
        #     if l in func and func[l]!=0:
        #         func[l]-=1
        #     else:
        #         return False
        # return True
    
    ##Approach 2: O(nlogn) sort both sting and compare if they are same or not.
        
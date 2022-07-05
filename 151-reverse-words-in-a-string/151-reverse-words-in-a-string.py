class Solution:
    def reverseWords(self, s: str) -> str:
        l=list(s.split(" "))
        final=[]
        for w in l:
            if w!='':
                final.append(w)
        
        return ' '.join(final[::-1])
        
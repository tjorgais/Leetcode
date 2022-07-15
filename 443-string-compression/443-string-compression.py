class Solution:
    def compress(self, chars: List[str]) -> int:
        n=len(chars)
        count=1
        compress=''
        i=0
        while(i!=n-1):
            if chars[i]==chars[i+1]:
                count+=1
            else:
                if count==1:
                    compress+=chars[i]
                else:
                    compress+=chars[i]+str(count)
                count=1
            i+=1
        
        if count==1:
            compress+=chars[i]
        else:
            compress+=chars[i]+str(count)
        chars.clear()
        chars[:0]=compress
        
        return len(compress)
                
            
        
        
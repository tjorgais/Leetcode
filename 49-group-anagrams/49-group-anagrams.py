class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        func={}
        for word in strs:
            
            x=''.join(sorted(word))
            arr=func.get(x,[])
            arr.append(word)
            func[x]=arr
        output=[]
        for key in func.keys():
            output.append((func[key]))
        return output
        
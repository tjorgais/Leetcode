class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        stack=[]
        for i in range(len(intervals)):
            if len(stack)==0:
                stack.append(intervals[i])
            else:
                element=stack.pop()
                if intervals[i][0]<=element[1]:
                    stack.append([element[0],max(element[1], intervals[i][1])])
                else:
                    stack.append(element)
                    stack.append(intervals[i])
        return stack

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        n = len(intervals)

        new_arr = []
        if n == 0:
            intervals.append(newInterval)
            return intervals
        else:
            inserted=False
            for i in range(n):
                if intervals[i][0] >= newInterval[0]:
                    new_arr.append(newInterval)

                    new_arr.append(intervals[i])
                    inserted=True
                else:
                    new_arr.append(intervals[i])
            if inserted==False:
                new_arr.append(newInterval)


            stack = []
            for i in range(len(new_arr)):
                if len(stack) == 0:
                    stack.append(new_arr[i])
                else:
                    element = stack.pop()
                    if new_arr[i][0] <= element[1]:
                        stack.append([element[0], max(element[1], new_arr[i][1])])
                    else:
                        stack.append(element)
                        stack.append(new_arr[i])

            return stack
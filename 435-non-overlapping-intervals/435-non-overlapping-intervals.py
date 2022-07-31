class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort()
        #print(intervals)
        count=0
        curr_y=intervals[0][1]
        for i in range(1, n):
            if intervals[i][0]>=curr_y:
                curr_y=intervals[i][1]
            elif intervals[i][1]<curr_y:
                count+=1
                curr_y=intervals[i][1]
            elif intervals[i][1]>=curr_y:
                count+=1
        return count
             
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = []
        intervals.sort(key = lambda x: x[0])
        count = 0
        ans.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0] >= ans[-1][1]:
                ans.append(intervals[i])
            else:
                count+=1
                if ans[-1][1]<intervals[i][1]:
                    continue
                else:
                    ans[-1][0] = intervals[i][0]
                    ans[-1][1] = intervals[i][1]
        return count



        
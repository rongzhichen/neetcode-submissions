class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        n = 1
        ans = [intervals[0]]
        while n < len(intervals):
            if intervals[n][0] > ans[-1][1]:
                ans.append(intervals[n])
                n+=1
                continue
            else:
                ans[-1][1] = max(ans[-1][1], intervals[n][1])
                n+=1
        return(ans)



        
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = len(intervals)
        if intervals == []:
            intervals.append(newInterval)
            return (intervals)

        for i in range(len(intervals)):
            if newInterval[0]<=intervals[i][0]:
                start = i
                break
        intervals.insert(start, newInterval)
        if newInterval[0]<= intervals[start-1][1] and start>0:
            intervals.pop(start)
            intervals[start-1] = [intervals[start-1][0], max(intervals[start-1][1], newInterval[1])]
            start-=1
        merge = True
        while merge and len(intervals)>1 and start < len(intervals)-1:
            if intervals[start+1][0]<=newInterval[1]:
                intervals[start][1] = max(newInterval[1], intervals[start+1][1])
                intervals.pop(start+1)
                continue
            merge = False

        return(intervals)
        
        
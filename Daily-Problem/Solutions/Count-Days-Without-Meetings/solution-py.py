class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        count = 0
        last = 0
        meetings.sort()
        for start,end in meetings:
            if start > last+1:
                count += start -last -1
            last = max(last,end)
        count += days - last

        return count


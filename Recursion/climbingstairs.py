class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        listt = [0]*(n+1)
        listt[1] = 1
        listt[2] = 2
        for i in range(3,n+1):
            listt[i]= listt[i-1]+listt[i-2]
        return listt[-1]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        n = 1
        for i in range(1,k):
            if nums[i] != nums[i-1]:
                nums[n]=nums[i]
                n+=1
        return n
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n= len(nums)
        i=0
        while i <len(nums):
            if val == nums[i]:
                nums.pop(i)
            else:
                i+=1

        return len(nums)
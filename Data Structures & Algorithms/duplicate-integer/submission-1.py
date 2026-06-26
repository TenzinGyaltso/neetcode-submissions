class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #sorting the numbers in the list
        nums.sort()

        #loop through and compare each number to the one right next to it
        for i in range(len(nums) - 1):

            if nums[i] == nums[i + 1]:
                return True

        return False
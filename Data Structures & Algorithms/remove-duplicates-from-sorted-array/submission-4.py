class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


      l = 1
      r = 1

      while r < len(nums):
        if nums[r] != nums[r - 1]:
          nums[l] = nums[r]
          l = l +1

        r = r + 1

      return l



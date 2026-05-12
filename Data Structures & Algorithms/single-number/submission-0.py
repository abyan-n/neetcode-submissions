class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        seenNums = {}

        for num in nums:
            if num in seenNums:
                seenNums[num] = seenNums[num] + 1
            else:
                seenNums[num] = 1
        

        for key, value in seenNums.items():
            if value == 1:
                return key
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = [0] * (len(nums) * 2)
        # 0, 1, 2, 3
        #[1, 4, 1, 2]

        # i in range 8
        # len(nums) = 4
        # i = 0
        # ans = [1]
        for i in range(len(nums) * 2):
            
            if i >= len(nums):
                ans[i] = nums[i - len(nums)]
            else:
                ans[i] = nums[i]


        return ans
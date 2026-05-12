class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = {}

        for index, num in enumerate(nums):
            if num in seen:

                if abs(index - seen[num]) <= k:
                    return True
                else:
                    seen.pop(num)
                    seen[num] = index
            else:
                seen[num] = index

        return False
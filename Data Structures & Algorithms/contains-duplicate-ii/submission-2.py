class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 1
        s = [nums[0]]
        while j < len(nums):
            if nums[j] in s:
                return True
            elif abs(i - j) < k:
                s.append(nums[j])
                j += 1
            else:
                s.pop(0)
                s.append(nums[j])
                i += 1
                j += 1
        return False
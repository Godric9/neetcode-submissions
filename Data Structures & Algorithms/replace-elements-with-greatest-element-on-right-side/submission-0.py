class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            m = -1
            for j in range(i + 1, len(arr)):
                if m < arr[j]:
                    m = arr[j]
            arr[i] = m
        return arr
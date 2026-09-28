class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        for i in range(l):
            m = -1
            for j in range(i + 1, l):
                m = max(m, arr[j])
            arr[i] = m
        return arr
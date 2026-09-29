class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        dq = deque()
        for log in logs:
            if "../" in log:
                count -= 1 if count != 0 else 0
            elif "./" in log:
                continue
            else:
                count += 1
        return count
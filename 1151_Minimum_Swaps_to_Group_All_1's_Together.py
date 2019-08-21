class Solution:
    def minSwaps(self, data) -> int:
        if sum(data) == 1: return 0

        N = len(data)
        target = sum(data)

        pre = res = target - sum(data[:target])
        i = 0
        while i + target < N:
            if data[i] == 0 and data[i+target] == 1:
                pre -= 1
                res = min(res, pre)
            elif data[i] == 1 and data[i+target] == 0:
                pre += 1
            i += 1
        return res
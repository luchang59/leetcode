class Solution:
    def judgePoint24(self, nums) -> bool:
        # 每次从list中取两个数字，进行加减乘除的操作，得出来的数字，放入下一次的操作
        # 当list只剩下一个元素，并且等于24的时候，返回True
        # 因为对于不能整除的小数，会四舍五入，所以结果会不是整数的24， 而是23.999999999999999或者24.0000000000000001
        # 所以答案要优化成 abs(path[0] - 24) < 1e-6

        def backTrack(path):
            if len(path) == 1 and abs(path[0] - 24) < 1e-6: return True
            if len(path) == 1 and abs(path[0] - 24) >= 1e-6: return False

            for i in range(len(path)):
                a = path[i]
                tmp = path[:i] + path[i+1:]
                for j in range(len(tmp)):
                    b = tmp[j]
                    newPath = tmp[:j] + tmp[j+1:]
                    if b == 0: continue
                    if backTrack(newPath + [a + b]): return True
                    if backTrack(newPath + [a - b]): return True
                    if backTrack(newPath + [a * b]): return True
                    if backTrack(newPath + [a / b]): return True
            return False

        return backTrack(nums) 
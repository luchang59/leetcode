class Solution:
    def twoSum(self, numbers, target):

        # two points
        first, second = 0, len(numbers) - 1

        while first < second:
            if numbers[first] + numbers[second] < target:
                first += 1
            elif numbers[first] + numbers[second] > target:
                second -= 1
            else:
                return [first + 1, second + 1]

        # binary search
        for i in range(len(numbers)):
            start, end = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while start < end:
                mid = start + (end - start) // 2
                if numbers[mid] == tmp:
                    return [start + 1, mid + 1]
                elif numbers[mid] < tmp:
                    start = mid + 1
                else:
                    end = mid - 1
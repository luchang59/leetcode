class Solution:
    def findKthLargest(self, nums, k: int) -> int:
    # convert the kth largest to smallest
        return self.findKthSmallest(nums, len(nums)+1-k)

    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums)-1)
            if k > pos+1:
                return self.findKthSmallest(nums[pos+1:], k-pos-1)
            elif k < pos+1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    # choose the right-most element as pivot   
    def partition(self, nums, l, r):
        low = l 
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low





    # 这算法叫做 快速选择
    # 把所有小于 最后一个数字的 丢到前面 然后大于的 丢到后面
    # 最后把最后一个数字 和 low最后所在位置的交换 那么最后一个数字就会到它应该在的位置
    #       5, 3, 4, 7, 2, 1, 6
    #      l, low             r
    #               low l     r
    #       5, 3, 4, 2, 7, 1, 6
    #                  low l  r
    #       5, 3, 4, 2, 1, 7, 6
    #                     low r      
    #     
class Solution:
    def intersection(self, nums1, nums2):

        dic, res = {}, []

        for n in nums1:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        
        for n in nums2:
            if n in dic:
                res.append(n)
                dic[n] -= 1
                if dic[n] == 0:
                    del dic[n]
        
        return res
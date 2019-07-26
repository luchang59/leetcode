class Solution:
    def findRestaurant(self, list1, list2):
        
        dic, count = {}, float('inf')

        for i, l in enumerate(list1):
            dic[l] = i
        
        for i, l in enumerate(list2):
            if l in dic:
                tmp = dic[l] + i
                if tmp < count:
                    res = []
                    res.append(l)
                    count = tmp
                elif tmp == count:
                    res.append(l)
        
        return res
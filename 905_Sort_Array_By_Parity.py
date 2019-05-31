class Solution:
    def sortArrayByParity(self, A):
#         My solution
#  
#         even = []
#         odd = []
        
#         for a in A:
#             if a % 2 == 1:
#                 odd.append(a)
#             else:
#                 even.append(a)
        
#         return even + odd

        A.sort(key = lambda x: x % 2)
        return A
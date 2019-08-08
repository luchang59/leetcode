class Solution:
    def grayCode(self, n):

        """
        eg:     1       2       3       res
                0       00      000     0
                1       01      001     1
                        11      011     3     
                        10      010     2
                                110     6
                                111     7
                                101     5
                                100     4
        The middle two numbers only differ at their highest bit, 
        while the rest numbers of part two are exactly symmetric of part one. It is easy to see its correctness.
        """

        res = [0]
        for i in range(n):
            new = []
            for x in reversed(res):
                new.append((x + pow(2, i)))
            res.extend(new)
            # res += new        # as some as prev line
        return res
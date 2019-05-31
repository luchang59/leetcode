class Solution:
    def numTrees(self, n: int) -> int:
        
        """
        state function:
        example:
        G(3) = F(1,3) + F(2,3) + F(3,3)
        F(i,n) means i is the root and 3 is the total number of nodes. It means how to build a BST as 1 is the root, 2 is the root and 3 is the root.
        And there is 3 nodes.
        Therefor F(i,n) = G(i-1) * G(n-1), for example, F(1, 3) = G(0) * G(2), means G(0 node) multiply G(2 node).
        G(0) = 1, G(1) = 1
        For n, return G(n)
        """

        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]
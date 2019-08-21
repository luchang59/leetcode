"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
Example 1:
Input:["wrt", "wrf", "er", "ett", "rftt"]
Output: "wertf"

Example 2:
Input:["z", "x"]
Output: "zx"

Example 3:
Input:["z", "x", "z"] 
Output: "" 
Explanation: The order is invalid, so return "".
"""
import collections
class Solution:
    def alienOrder(self, words):
        if not words: return ""

        dic = {}
        degree = {}
        res = ""

        for word in words:
            for letter in word:
                dic.setdefault(letter, set())
                degree.setdefault(letter, 0)
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            length = min(len(word1), len(word2))
            for j in range(length):
                if word1[j] != word2[j]:
                    if word2[j] not in word1[j]:
                        dic[word1].add(word2)
                        degree[word2] += 1
                    break
        
        queue = collections.deque()
        for letter in degree.keys():
            if degree[letter] == 0:
                queue.append(letter)
                del degree[letter]

        while queue:
            letter = queue.popleft()
            res += letter
            for nxt in dic[letter]:
                degree[nxt] -= 1
                if degree[nxt] == 0:
                    queue.append(nxt)
                    del degree[letter]
        
        return res if not degree else ""
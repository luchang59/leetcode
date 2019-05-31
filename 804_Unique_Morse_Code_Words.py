import collections
class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        hashset = collections.defaultdict()
        
        for i in range(len(code)):
            hashset[alphabet[i]] = code[i]
            
        seen = set()
        
        for word in words:
            tmp = ''
            for c in word:
                tmp += hashset[c]
            seen.add(tmp)
        
        return len(seen)
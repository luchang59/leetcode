import collections

class Solutions:
    def ladderLength(self, beginWord, endWord, wordList):

        if endWord not in wordList or not beginWord or not endWord or not wordList: return 0

        allWords = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                newWord = word[:i] + '*' + word[i+1:]
                allWords[newWord].append(word)
        
        queue = collections.deque([(beginWord, 1)])
        seen = set([beginWord])

        while queue:
            word, step = queue.popleft()
            if word == endWord: return step
            
            for i in range(len(word)):
                newWord = word[:i] + '*' + word[i+1:]
                for curWord in allWords[newWord]:
                    if curWord not in seen:
                        seen.add(curWord)
                        queue.append((curWord, step + 1))
        
        return 0
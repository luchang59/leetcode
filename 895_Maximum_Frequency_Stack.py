import collections
class FreqStack:
    
    def __init__(self):
        self.dict = collections.defaultdict(int)
        self.freq = collections.defaultdict(list)
        self.maxi = 0
    
    def push(self, x):
        self.dict[x] += 1
        if self.dict[x] > self.maxi:
            self.maxi += 1
        self.freq[self.dict[x]].append(x)
    
    def pop(self):
        x = self.freq[self.maxi].pop()
        self.dict[x] -= 1
        if not self.freq[self.maxi]:
            self.maxi -= 1
        return x
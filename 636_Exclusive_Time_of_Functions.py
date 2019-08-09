class Solution:
    def exlusiveTime(self, n, logs):
        
        """
        log: {id:start | end: time}
        """

        res = [0] * n
        prev = 0
        stack = []

        for l in logs:
            idx, state, time = l.split(':')
            if state == 'start':
                if stack:
                    res[stack[-1]] += int(time) - prev
                prev = int(time)
                stack.append(int(idx))
            else:
                res[stack.pop()] += int(time) - prev + 1
                prev = int(time) + 1
        
        return res
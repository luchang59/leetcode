class Solution:
    def validUtf8(self, data) -> bool:
        count = 0
        for d in data:
            d = bin(d)[2:]
            if len(d) < 8:
                d = '0' * (8 - len(d)) + d
            if count == 0:
                for c in d:
                    if c == '0': break
                    count += 1
                if count == 0: continue
                if count == 1 or count > 4:
                    return False
            else:
                if d[:2] != '10':
                    return False
            count -= 1
        return count == 0
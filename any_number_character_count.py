from collections import Counter


class Solution:
    def commonChars(self, A):
        minimum_len = min(len(x) for x in A)
        small = ""

        # find the item with the minimum length
        for item in A:
            if len(item) == minimum_len:
                small = item

        # find the item
        k = Counter(small)
        for word in A:
            for key in k:
                if word.count(key) < k[key]:
                    k[key] = word.count(key)
                else:
                    k[key] = 0

        l = []
        for item in k:
            l += [item] * k[item]
        return l


s = Solution()

print(s.commonChars(["cool","lock","cook"]))
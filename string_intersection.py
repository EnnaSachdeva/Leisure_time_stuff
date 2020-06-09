class Solution:
    def intersect(self, nums1, nums2):
        output = []
        count_a = {}
        count_b = {}

        for item in nums1:
            count_a[item] = 0

        for item in nums2:
            count_b[item] = 0

        for item in nums1:
            count_a[item] += 1

        for item in nums2:
            count_b[item] += 1

        for key, value in count_a.items():
            if (key in count_a) and (key in count_b):
                print(count_a[key], count_b[key])
                if (count_a[key] <= count_b[key]):
                    [output.append(key) for _ in range(count_a[key])]
                else:
                    [output.append(key) for _ in range(count_b[key])]

        return output

s = Solution()

s.intersect([4,9,5], [9,4,9,8,4])

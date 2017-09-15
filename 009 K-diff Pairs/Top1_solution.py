# 很精妙的解法。 使用到了collections 模块。
# 比我的解法提高20% 效率。

def findPairs(nums, k):
    return  len(set(nums) & {n+k for n in nums}) if k > 0  \
            else sum(v > 1 for v in collections.Counter(nums).values()) if k == 0  \
            else 0

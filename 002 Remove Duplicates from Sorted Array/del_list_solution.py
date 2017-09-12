# 尝试了删除多余元素的方法， 结果是del删除会更快。 

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                #nums.pop(i)  # beat 34%
                del(nums[i])  # beat 50% 
                #nums.remove(nums[i-1]) # Time Limit Exceeded.

        if len(nums) >= 2 and nums[0] == nums[1]:
            nums.pop(0)

        return len(nums)
    
    
# for循环遍历时删除导致索引变化，解决办法：
# 1. while，  删除后i -= 1
# 2. for 倒序删除
# 3. 遍历拷贝的list，删除原始的list    
        

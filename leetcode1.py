class Solution:
    def twoSum(self, nums, target):
        li=[]
        l = len(nums)
        for x in range(l):
            if target-nums[x] in nums:
                # print ("@")
                li=[x,nums.index(target-nums[x])]
                # print ([x,)
                if li[0]==li[1]:
                    pass
                else:
                    return li
        return li

sol = Solution()

nums = [2, 7, 11, 15]
target = 9

print (sol.twoSum(nums, target))

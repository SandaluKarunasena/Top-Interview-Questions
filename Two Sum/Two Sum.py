class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            number = target - nums[i]
            if number in dic:
                return [dic[number],i]
            dic[nums[i]]=i

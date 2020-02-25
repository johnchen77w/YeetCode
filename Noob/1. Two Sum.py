def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        size = len(nums)
        for i in range(size):
            diff = target - nums[i]
            if diff in dic:
                index = dic[diff]
                return [index, i]
            else:
                dic[nums[i]] = i

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        pair = len(nums) / 2
        hashMap = {}
        flag = 0
        for num in nums:
            if num in hashMap.keys():
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        for value in hashMap.values():
            if flag % 2 != 0:
                return False
            else:
                flag += value
        return True
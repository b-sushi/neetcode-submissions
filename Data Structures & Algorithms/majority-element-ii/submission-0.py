class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        n = len(nums)
        cutoff = math.floor(n/3)
        ans = []
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        for key, val in dic.items():
            if val > cutoff:
                ans.append(key)
        return ans
'''
1st instinct is just to solve this by looping through w a dictionary, making a key:value pair where key is frequency, value is the number and then just looping through the dictionary and returning all the valid values



'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num_freq = {}
        count_to_num = [[] for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            num_freq[nums[i]] = 1+ num_freq.get(nums[i], 0)

        for key, value in num_freq.items():
            count_to_num[value].append(key)

        res = []
        for i in range(len(count_to_num) -1, 0, -1):
            for num in count_to_num[i]:
                res.append(num)
                if len(res) == k:
                    return res


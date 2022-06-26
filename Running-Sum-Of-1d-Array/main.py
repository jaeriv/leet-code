class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        final_list = []

        for index, value in enumerate(nums):
            before_value = nums[:index]
            total_before = sum(before_value)
            final_list.append(total_before + value)
        return final_list

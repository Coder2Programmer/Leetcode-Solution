class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask = 0
        for num in nums:
            mask ^= num
        mask &= -mask
        
        first_number = second_number = 0
        for num in nums:
            if num & mask:
                first_number ^= num
            else:
                second_number ^= num
        
        return [first_number, second_number]
        
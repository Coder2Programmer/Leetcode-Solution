class String(str):
    def __init__(self, number: int):
        self.value = str(number)
    
    def __lt__(self, string: 'String'):
        return self.value + string.value < string.value + self.value
    
    def __gt__(self, string: 'String'):
        return self.value + string.value > string.value + self.value
    
    def __eq__(self, string: 'String'):
        return self.value + string.value == string.value + self.value
    
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return ''.join(sorted([String(num) for num in nums], reverse=True)).lstrip('0') or '0'
    
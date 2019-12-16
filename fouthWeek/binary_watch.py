class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        return [f'{hour}:{minute:02d}' 
                for hour in range(12) 
                for minute in range(60) 
                if bin(hour).count('1') + bin(minute).count('1') == num]
                
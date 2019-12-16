class Solution:
    def __init__(self):
        self.ip_list = list()
        self.field_list = list()
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.helper(s, 4)
        return self.ip_list
    
    def helper(self, s: str, remain_number: int) -> None:
        if remain_number <= 0:
            if s == '':
                self.ip_list.append('.'.join(self.field_list))
            return
        
        for i in range(1, min(4, len(s) + 1)):
            if i >= 3 and int(s[:i]) > 255:
                return
            self.field_list.append(s[:i])
            self.helper(s[i:], remain_number - 1)
            self.field_list.pop()
            if s[0] == '0':
                return
                
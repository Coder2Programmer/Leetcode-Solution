class Solution:
    ipv4_seg = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    ipv4_pattern = re.compile(r'^(' + ipv4_seg + r'\.){3}' + ipv4_seg + r'$')
    ipv6_seg = r'([0-9a-fA-F]{1,4})'
    ipv6_pattern = re.compile(r'^(' + ipv6_seg + r'\:){7}' + ipv6_seg + r'$')
    def validIPAddress(self, IP: str) -> str:
        if self.ipv4_pattern.match(IP):
            return 'IPv4'
        if self.ipv6_pattern.match(IP):
            return 'IPv6'
        return 'Neither'
        
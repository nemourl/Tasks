import re


def valid_ipv4(ip):
    pattern = (
        r'^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
        r'(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$'
    )

    return bool(re.fullmatch(pattern, ip))

print(valid_ipv4("192.168.0.1"))        
print(valid_ipv4("255.255.255.255"))    
print(valid_ipv4("256.100.50.0"))       
print(valid_ipv4("01.1.1.1"))           
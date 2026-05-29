import re


def strong_password(password):
    pattern = (
        r'^(?=.*\d)'          
        r'(?=.*[a-z])'        
        r'(?=.*[A-Z])'        
        r'[A-Za-z\d_]{8,}$'   
    )

    return bool(re.fullmatch(pattern, password))

print(strong_password("Abc12345"))     
print(strong_password("password"))     
print(strong_password("ABC12345"))     
print(strong_password("Abc_1234"))     
print(strong_password("Abc-1234"))     
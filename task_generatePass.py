import random
import string

def generate_password(length = 12):
    special_chars = "!@#$%^&*()-_=+"

    if length < 4:
        raise ValueError("Пароль не может быть короче 4 символов")

    all_chars = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        special_chars
    )

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(special_chars)
    ]

    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    print(generate_password())     
    print(generate_password(8))     
    print(generate_password(16))    
    print(generate_password(4))     
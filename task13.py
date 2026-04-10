word = input("Введите слово на латинице: ")
shift = int(input("Введите сдвиг (от 1 до 10): "))

if shift < 1 or shift > 10:
    print("Ошибка: сдвиг должен быть от 1 до 10")
else:
    only_latin = True
    for ch in word:
        if not (('a' <= ch <= 'z') or ('A' <= ch <= 'Z')):
            only_latin = False
            break
    
    if not only_latin:
        print("Ошибка: используйте только латинские буквы")
    else:
        encrypted = ""
        for ch in word:
            if 'A' <= ch <= 'Z':
                num = ord(ch) - ord('A')
                new_num = (num + shift) % 26
                new_ch = chr(new_num + ord('A'))
                encrypted = encrypted + new_ch
            else:
                num = ord(ch) - ord('a')
                new_num = (num + shift) % 26
                new_ch = chr(new_num + ord('a'))
                encrypted = encrypted + new_ch
        
        print("Зашифрованное слово:", encrypted)
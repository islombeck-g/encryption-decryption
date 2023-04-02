# 9. Алгоритм шифрования, шифр простой перестановки, без добавления нулей, отдельный символ
# 10. Алгоритм расшифровывания, шифр простой перестановки, без добавления нулей, отдельный символ


def generate_key():
    # генерация ключа
    key = list(set("BADCsomeKeyd"))
    return key

def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char in key:
            # заменяем символ на соответствующий символ в ключе
            index = key.index(char)
            result += key[(index + 1) % len(key)]  # выполняем циклический сдвиг
        else:
            # оставляем символ без изменений
            result += char
    return result

def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char in key:
            # заменяем символ на соответствующий символ в ключе
            index = key.index(char)
            result += key[(index - 1) % len(key)]  # выполняем циклический сдвиг
        else:
            # оставляем символ без изменений
            result += char
    return result


key = generate_key()

text = "some Text"
encriptedText = encrypt(text, key)
print(encriptedText)
decriptedText = decrypt(encriptedText, key)
print(decriptedText)


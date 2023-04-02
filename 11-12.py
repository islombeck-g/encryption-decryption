# 11. Алгоритм шифрования, шифр простой перестановки, без добавления нулей, группа из произвольного количества символов
# 12. Алгоритм расшифровывания, шифр простой перестановки, без добавления нулей, группа из произвольного количества символов



BLOCK_SIZE = 16

def generate_key():
    # генерация ключа
    key = list(set("BADCsomeKыdsafeyd"))
    return key

def pad(text):
    # дополнение текста до размера, кратного BLOCK_SIZE
    padding_size = BLOCK_SIZE - len(text) % BLOCK_SIZE
    padding = chr(padding_size) * padding_size
    return text + padding

def unpad(padded_text):
    # удаление дополнения из текста
    padding_size = ord(padded_text[-1])
    return padded_text[:-padding_size]

def encrypt(plaintext, key):
    padded_text = pad(plaintext)
    result = ""
    for i in range(0, len(padded_text), BLOCK_SIZE):
        block = padded_text[i:i+BLOCK_SIZE]
        encrypted_block = ""
        for char in block:
            if char in key:
                # заменяем символ на соответствующий символ в ключе
                index = key.index(char)
                encrypted_block += key[(index + 1) % len(key)]  # выполняем циклический сдвиг
            else:
                # оставляем символ без изменений
                encrypted_block += char
        result += encrypted_block
    return result

def decrypt(ciphertext, key):
    result = ""
    for i in range(0, len(ciphertext), BLOCK_SIZE):
        block = ciphertext[i:i+BLOCK_SIZE]
        decrypted_block = ""
        for char in block:
            if char in key:
                # заменяем символ на соответствующий символ в ключе
                index = key.index(char)
                decrypted_block += key[(index - 1) % len(key)]  # выполняем циклический сдвиг
            else:
                # оставляем символ без изменений
                decrypted_block += char
        result += decrypted_block
    return unpad(result)


key = generate_key()

text = "some Text"
encrypted_text = encrypt(text, key)

decrypted_text = decrypt(encrypted_text, key)
print("text: "+ text)
print("encrypted_text: " + encrypted_text)
print("decripted_text: " + decrypted_text)

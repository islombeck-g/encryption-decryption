# 1  - Алгоритм шифрования, шифр простой перестановки, с добавлением нулей, отдельный символ
# 2  - Алгоритм расшифровывания, шифр простой перестановки, с добавлением нулей, отдельный символ

def pad_block(block, block_size): #добавление нулей, если размер меньше длины ключа
    padding_size = block_size - len(block)
    return block + '0' * padding_size


def encrypt(plaintext, key):
    # шифруем
    block_size = len(key)
    key_indices = sorted(range(len(key)), key=lambda k: key[k])
    result = ""

    for i in range(0, len(plaintext), block_size):

        block = plaintext[i:i + block_size] # извлечение блока из открытого текста.
        if len(block) < block_size:
            block = pad_block(block, block_size)

        for index in key_indices:
            result += block[index]# добавление символа из текущего блока в зашифрованный текст согласно порядку, определенному ключом.


    return result


def decrypt(ciphertext, key):
    block_size = len(key)
    key_indices = sorted(range(len(key)), key=lambda k: key[k])
    plaintext = ""

    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i+block_size]
        decrypted_block = [''] * block_size

        for index, char in zip(key_indices, block):
            decrypted_block[index] = char

        plaintext += ''.join(decrypted_block)

    return plaintext.rstrip('0')


key = "3134324234"

plaintext = "Hello, World!"
encryptedText = encrypt(plaintext, key)
decrypted_text = decrypt(encryptedText, key)

print("Зашифрованный текст:", encryptedText)
print("расшифрованный текст:", decrypted_text)




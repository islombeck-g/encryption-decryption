# 3. Алгоритм шифрования, шифр простой перестановки, с добавлением нулей, группа из произвольного количества символов
# 4. Алгоритм расшифровывания, шифр простой перестановки, с добавлением нулей, группа из произвольного количества символов



def pad_block(block, block_size): # добавление нулей, если размер меньше длины блока
    padding_size = block_size - len(block)
    return block + '0' * padding_size


def encrypt(someText, key, block_size):
    # шифруем
    key_indices = sorted(range(len(key)), key=lambda k: key[k])
    result = ""

    for i in range(0, len(someText), block_size):

        block = someText[i:i + block_size] # извлечение блока из открытого текста.

        if len(block) < block_size:
            block = pad_block(block, block_size)

        for index in key_indices:
            result += block[index] # добавление символа из текущего блока в зашифрованный текст согласно порядку, определенному ключом.

    return result


def decrypt(ciphertext, key, block_size):
    key_indices = sorted(range(len(key)), key=lambda k: key[k])
    result = ""

    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i+block_size]
        decrypted_block = [''] * block_size

        for index, char in zip(key_indices, block):
            decrypted_block[index] = char

        result += ''.join(decrypted_block)

    return result.rstrip('0')


key = "adfdfdfdfsgsdfh"
BLOCK_SIZE = 16

text = "Islam is here"
encrypted_text = encrypt(text, key, BLOCK_SIZE)
decrypted_text = decrypt(encrypted_text, key, BLOCK_SIZE)
print("текст: ", text)
print("Зашифрованный текст:", encrypted_text)
print("Расшифрованный текст:", decrypted_text)
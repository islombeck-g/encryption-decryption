# 5. Алгоритм шифрования, шифр простой перестановки, с добавлением нулей, байт
# 6. Алгоритм расшифровывания, шифр простой перестановки, с добавлением нулей, байт

def generate_permutation_table(key):
    # Формируем таблицу перестановок на основе ключа
    table = {}
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=_+[]{}|;':\",./<>?\\ "
    for i in range(len(alphabet)):
        table[alphabet[i]] = alphabet[(i + key) % len(alphabet)]
    return table

def add_zeros(message):
    # Добавляем нули между байтами сообщения
    return "0".join(message)

def remove_zeros(message):
    # Удаляем все нули из расшифрованного сообщения
    return message.replace("0", "")

def encrypt(message, key):
    # Шифруем сообщение
    permutation_table = generate_permutation_table(key)
    message_with_zeros = add_zeros(message)
    result = ""
    for char in message_with_zeros:
        # Заменяем каждый символ сообщения на соответствующий ему символ в таблице перестановок
        if char in permutation_table:
            result += permutation_table[char]
    return result

def decrypt(message, key):
    # Расшифровываем сообщение
    permutation_table = generate_permutation_table(key)
    # Создаем обратную таблицу перестановок
    reverse_table = {}
    for char in permutation_table:
        reverse_table[permutation_table[char]] = char
    result = ""
    for char in message:
        # Заменяем каждый символ зашифрованного сообщения на соответствующий ему символ в обратной таблице перестановок
        if char in reverse_table:
            result += reverse_table[char]
    # Удаляем все нули из расшифрованного сообщения
    result = remove_zeros(result)
    return result

key = 5
text = "Islam was here"
encrypted_message = encrypt(text, key)
decrypted_message = decrypt(encrypted_message, key)
print(f"Зашифрованное сообщение: {encrypted_message}")
print(f"Расшифрованное сообщение: {decrypted_message}")

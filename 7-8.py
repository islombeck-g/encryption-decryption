# 7. Алгоритм шифрования, шифр простой перестановки, с добавлением нулей, бит
# 8. Алгоритм расшифровывания, шифр простой перестановки, с добавлением нулей, бит


def generate_permutation_table(key):
    # Генерируем таблицу перестановок на основе ключа
    permutation_table = {}
    # Заполняем таблицу символами от ' ' до '~'
    available_chars = [chr(i) for i in range(32, 127)]
    for i, char in enumerate(available_chars):
        # Вычисляем индекс нового символа в таблице перестановок
        new_index = (i + key) % len(available_chars)
        permutation_table[char] = available_chars[new_index]
    return permutation_table


def encrypt(message, key):
    # Шифруем сообщение
    permutation_table = generate_permutation_table(key)
    result = ""
    for char in message:
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
    return result


key = 5
text = "Islombek was there"
encrypted_message = encrypt(text, key)
decrypted_message = decrypt(encrypted_message, key)
print(f"Зашифрованное сообщение: {encrypted_message}")
print(f"Расшифрованное сообщение: {decrypted_message}")

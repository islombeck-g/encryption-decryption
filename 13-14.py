# 13. Алгоритм шифрования, шифр простой перестановки, без добавления нулей, байт
# 14. Алгоритм расшифровывания, шифр простой перестановки, без добавления нулей, байт

# изза того что мы не можем добавить нули, он ток работает если длина шифруемого текста нацело делится на длину ключа
def encrypt(text, key):
    key_len = len(key)
    encrypted_text = ""
    for i in range(0, len(text), key_len):
        group = text[i:i+key_len]
        encrypted_group = "".join([group[int(k)-1] for k in key])
        encrypted_text += encrypted_group
    return encrypted_text



def decrypt(text, key):
    key_len = len(key)
    decrypted_text = ""
    for i in range(0, len(text), key_len):
        group = text[i:i+key_len]
        decrypted_group = [''] * key_len
        for j, k in enumerate(key):
            decrypted_group[int(k)-1] = group[j]
        decrypted_text += "".join(decrypted_group)
    return decrypted_text

plaintext = "islamIshere)"
key = "4132"
encrypted = encrypt(plaintext, key)
print(encrypted)
decrypted = decrypt(encrypted, key)
print(decrypted)
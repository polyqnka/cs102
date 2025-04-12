"""
vigenere.py

Реализует шифр Виженера для шифрования и расшифровки текста.
"""


def _extend_key(text: str, key: str) -> str:
    """
    Расширяет ключ до длины текста, повторяя его по мере необходимости.

    """
    extended_key = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            extended_key += key[key_index % len(key)].upper()
            key_index += 1
        else:
            extended_key += char

    return extended_key


def encrypt_vigenere(plain_text: str, cipher_key: str) -> str:
    """
    Шифрует текст с использованием шифра Виженера.

    Примеры:
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    extended_key = _extend_key(plain_text, cipher_key)
    encrypted_message = ""

    for p_char, k_char in zip(plain_text, extended_key):
        if p_char.isalpha():
            shift = ord(k_char) - ord('A')
            new_char = chr((ord(p_char.upper()) - ord('A') + shift) % 26 + ord('A'))
            encrypted_message += new_char if p_char.isupper() else new_char.lower()
        else:
            encrypted_message += p_char
    return encrypted_message


def decrypt_vigenere(encrypted_text: str, cipher_key: str) -> str:
    """
    Расшифровывает текст, зашифрованный шифром Виженера.

    Примеры:
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    extended_key = _extend_key(encrypted_text, cipher_key)
    decrypted_message = ""

    for c_char, k_char in zip(encrypted_text, extended_key):
        if c_char.isalpha():
            shift = ord(k_char) - ord('A')
            new_char = chr((ord(c_char.upper()) - ord('A') - shift + 26) % 26 + ord('A'))
            decrypted_message += new_char if c_char.isupper() else new_char.lower()
        else:
            decrypted_message += c_char

    return decrypted_message


if __name__ == "__main__":
    ORIGINAL_TEXT = "ATTACKATDAWN"
    CIPHER_KEY = "LEMON"

    encrypted_message = encrypt_vigenere(ORIGINAL_TEXT, CIPHER_KEY)
    print(f"Зашифрованный текст: {encrypted_message}")

    decrypted_message = decrypt_vigenere(encrypted_message, CIPHER_KEY)
    print(f"Расшифрованный текст: {decrypted_message}")


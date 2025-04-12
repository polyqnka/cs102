"""caesar.py

Реализует шифровку и расшифровкку на шифре Цезаря

"""

def encrypt_caesar(plaintext="PYTHON", shift=3):

    """
    Encrypts plaintext using a Caesar cipher.
    Example: PYTHON -> SBWKRQ
    """

    ciphertext = ""
    for _ in plaintext:
        if "A" <= _ <= "Z":
            ciphertext += chr((ord(_) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= _ <= "z":
            ciphertext += chr((ord(_) - ord("a") + shift) % 26 + ord("a"))
        else:
            ciphertext += _
    return ciphertext


def decrypt_caesar(ciphertext="SBWKRQ", shift=3):

    """
    Decrypts a ciphertext using a Caesar cipher.
    Example: SBWKRQ -> PYTHON
    """

    plaintext = ""
    for _ in ciphertext:
        if "A" <= _ <= "Z":
            plaintext += chr((ord(_) - ord("A") - shift) % 26 + ord("A"))
        elif "a" <= _ <= "z":
            plaintext += chr((ord(_) - ord("a") - shift) % 26 + ord("a"))
        else:
            plaintext += _
    return plaintext

print(encrypt_caesar("PYTHON"))
print(decrypt_caesar("SBWKRQ"))

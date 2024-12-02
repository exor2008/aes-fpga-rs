from main import aes, expand_key


def test_aes_v1():
    key = bytearray("1000000000000000" * 11, "ascii")
    expand_key(key)
    plaintext = bytearray("0000000000000001", "ascii")
    ciphertext = aes(plaintext, key)
    assert ciphertext.hex().upper() == "25B57F9CEE2DEF1B6DC3B0E526EA9550"


def test_aes_v2():
    key = bytearray("0000000000000000" * 11, "ascii")
    expand_key(key)
    plaintext = bytearray("0000000000000000", "ascii")
    ciphertext = aes(plaintext, key)
    assert ciphertext.hex().upper() == "F95C7F6B192B22BFFEFD1B779933FBFC"


def test_aes_v3():
    key = bytearray("0123456789abcdef" * 11, "ascii")
    expand_key(key)
    plaintext = bytearray("fedcba9876543210", "ascii")
    ciphertext = aes(plaintext, key)
    assert ciphertext.hex().upper() == "0B4BD671F6707F09B838C3D6CA1C6A3D"

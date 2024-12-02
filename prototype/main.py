from enum import Enum

import numpy as np

from prototype.tables import SBOX


class KeyType(Enum):
    K128 = 1
    K192 = 2
    K256 = 3


def gmul(a: int, b: int):
    p = 0
    for _ in range(8):
        if (b & 1) == 1:
            p ^= a

        hi_bit_set = a & 0x80
        a <<= 1
        a &= 0xFF

        if hi_bit_set == 0x80:
            a ^= 0x1B

        b >>= 1

    return p


def gmul2(a: int):
    match a:
        case 1:
            return 2
        case 2:
            return 4
        case 4:
            return 8
        case 8:
            return 16
        case 16:
            return 32
        case 32:
            return 64
        case 64:
            return 128
        case 128:
            return 27
        case 27:
            return 54


def rcon(a: int) -> int:
    c = 1
    if a == 0:
        return 0
    while a != 1:
        c = gmul2(c)
        a -= 1
    return c


def rotate(word: bytearray) -> bytearray:
    return word[1:] + word[:1]


def schedule_core(word: bytearray, i: int) -> bytearray:
    word = rotate(word)

    r = [SBOX[bt] for bt in word]

    r[0] ^= rcon(i)

    return bytearray(r)


def expand_key(key: bytearray, key_type: KeyType = KeyType.K128):
    match key_type:
        case KeyType.K128:
            C_WORD = 16
            C_MAX = 176
        case KeyType.K192:
            C_WORD = 24
            C_MAX = 208
        case KeyType.K256:
            C_WORD = 32
            C_MAX = 240

    i = 1
    c = C_WORD

    while c < C_MAX:
        t = key[c - 4 : c]

        if c % C_WORD == 0:
            t = schedule_core(t, i)
            i += 1

        if key_type == KeyType.K256:
            if c % C_WORD == 16:
                t = bytearray([SBOX[bt] for bt in t])

        key_from = c - C_WORD
        key_to = c - C_WORD + 4
        key[c : c + 4] = [a ^ b for a, b in zip(key[key_from:key_to], t)]
        c += 4


def add_key(chunk: np.ndarray, key: np.ndarray) -> np.ndarray:
    if chunk.shape != key.shape:
        a = 0
    return chunk ^ key


def sub_bytes(chunk: np.ndarray):
    for i in range(4):
        for j in range(4):
            chunk[i, j] = SBOX[chunk[i, j]]


def shift_rows(chunk: np.ndarray) -> np.ndarray:
    return np.vstack(
        [
            chunk[0, :],
            np.roll(chunk[1, :], -1),
            np.roll(chunk[2, :], -2),
            np.roll(chunk[3, :], -3),
        ]
    )


def mix_column(column: np.ndarray) -> np.ndarray:
    a = np.zeros(4, dtype=np.uint8)
    b = np.zeros(4, dtype=np.uint8)
    c = np.zeros(4, dtype=np.uint8)

    for i in range(4):
        a[i] = column[i]
        h = column[i] & 0x80
        s = column[i] << 1
        b[i] = s & 0xFF

        if h == 0x80:
            b[i] ^= 0x1B

        c[0] = b[0] ^ a[3] ^ a[2] ^ b[1] ^ a[1]
        c[1] = b[1] ^ a[0] ^ a[3] ^ b[2] ^ a[2]
        c[2] = b[2] ^ a[1] ^ a[0] ^ b[3] ^ a[3]
        c[3] = b[3] ^ a[2] ^ a[1] ^ b[0] ^ a[0]

    return c


def to_16x16_matrix(bytes: bytearray) -> np.ndarray:
    arr = np.asarray(bytes)
    return arr.reshape(4, -1).T


def from_16x16_matrix(arr: np.ndarray) -> bytearray:
    return bytearray(arr.T.ravel())


def initial_round(plaintext: np.ndarray, key: np.ndarray) -> np.ndarray:
    return add_key(plaintext, key)


def normal_round(plaintext: np.ndarray, key: np.ndarray) -> np.ndarray:
    sub_bytes(plaintext)
    plaintext = shift_rows(plaintext)

    plaintext[:, 0] = mix_column(plaintext[:, 0])
    plaintext[:, 1] = mix_column(plaintext[:, 1])
    plaintext[:, 2] = mix_column(plaintext[:, 2])
    plaintext[:, 3] = mix_column(plaintext[:, 3])

    return add_key(plaintext, key)


def final_round(plaintext: np.ndarray, key: np.ndarray) -> np.ndarray:
    sub_bytes(plaintext)
    plaintext = shift_rows(plaintext)
    return add_key(plaintext, key)


def aes(plaintext_bytes: bytearray, key: bytearray) -> bytearray:
    plaintext = to_16x16_matrix(plaintext_bytes)
    plaintext = initial_round(plaintext, to_16x16_matrix(key[:16]))

    for i in range(1, 10):
        plaintext = normal_round(plaintext, to_16x16_matrix(key[i * 16 : (i + 1) * 16]))

    ciphertext = final_round(plaintext, to_16x16_matrix(key[10 * 16 : 11 * 16]))
    return from_16x16_matrix(ciphertext)


if __name__ == "__main__":
    # fmt: off
    key = bytearray("1000000000000000" * 11, "ascii")
    expand_key(key)

    plaintext = bytearray("0000000000000001", "ascii")
    # fmt: on

    ciphertext = aes(plaintext, key)

    print(ciphertext.hex(), ciphertext)

from enum import Enum

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


def add_key(chunk: bytearray, key: bytearray) -> bytearray:
    return bytearray([a ^ b for a, b in zip(chunk, key)])


def sub_bytes(chunk: bytearray) -> bytearray:
    return bytearray([SBOX[bt] for bt in chunk])


def shift_rows(chunk: bytearray) -> bytearray:
    return (
        chunk[:4]
        + chunk[5:8]
        + chunk[4:4]
        + chunk[10:12]
        + chunk[8:10]
        + chunk[15:15]
        + chunk[12:15]
    )


def mix_column(column: bytearray) -> bytearray:
    a = bytearray([0] * 4)
    b = bytearray([0] * 4)
    c = bytearray([0] * 4)

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


if __name__ == "__main__":
    print(f"R: {gmul(128, 3)}")

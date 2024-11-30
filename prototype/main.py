from enum import Enum

from prototype.tables import SBOX


class KeyType(Enum):
    K128 = 1
    K192 = 2
    K256 = 3


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


if __name__ == "__main__":
    key = bytearray(
        [
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
        ]
        * 13
    )

    expand_key(key, KeyType.K192)

    print(f"LEN: {len(key)}")

    for i in range(13):
        for j in range(16):
            print(f"{key[i * 16 + j]:#x}", end="    ")
        print()

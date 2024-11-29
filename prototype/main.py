from prototype.tables import SBOX


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

    print(r, i)

    return bytearray(r)


def expand_key(key: bytearray):
    c = 16
    i = 1

    while c < 176:
        t = key[c - 4 : c]

        if c % 16 == 0:
            t = schedule_core(t, i)
            i += 1

        key[c : c + 4] = [a ^ b for a, b in zip(key[c - 16 : c - 12], t)]
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
        ]
        * 11
    )

    expand_key(key)

    for i in range(11):
        for j in range(16):
            print(f"{key[i * 16 + j]:#x}", end="    ")
        print()

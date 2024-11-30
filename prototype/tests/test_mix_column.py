from main import mix_column


def test_mix_column_v1():
    EXPECTED_COLUMN = bytearray([0x8E, 0x4D, 0xA1, 0xBC])
    column = bytearray([0xDB, 0x13, 0x53, 0x45])
    mixed_column = mix_column(column)

    assert mixed_column == EXPECTED_COLUMN


def test_mix_column_v2():
    EXPECTED_COLUMN = bytearray([0x9F, 0xDC, 0x58, 0x9D])
    column = bytearray([0xF2, 0x0A, 0x22, 0x5C])
    mixed_column = mix_column(column)

    assert mixed_column == EXPECTED_COLUMN


def test_mix_column_v3():
    EXPECTED_COLUMN = bytearray([0x01, 0x01, 0x01, 0x01])
    column = bytearray([0x01, 0x01, 0x01, 0x01])
    mixed_column = mix_column(column)

    assert mixed_column == EXPECTED_COLUMN


def test_mix_column_v4():
    EXPECTED_COLUMN = bytearray([0xC6, 0xC6, 0xC6, 0xC6])
    column = bytearray([0xC6, 0xC6, 0xC6, 0xC6])
    mixed_column = mix_column(column)

    assert mixed_column == EXPECTED_COLUMN


def test_mix_column_v5():
    EXPECTED_COLUMN = bytearray([0xD5, 0xD5, 0xD7, 0xD6])
    column = bytearray([0xD4, 0xD4, 0xD4, 0xD5])
    mixed_column = mix_column(column)

    assert mixed_column == EXPECTED_COLUMN


def test_mix_column_v6():
    EXPECTED_COLUMN = bytearray([0x4D, 0x7E, 0xBD, 0xF8])
    column = bytearray([0x2D, 0x26, 0x31, 0x4C])
    mixed_column = mix_column(column)

    assert mixed_column == EXPECTED_COLUMN

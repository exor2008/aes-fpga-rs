import numpy as np

from main import from_16x16_matrix, shift_rows, to_16x16_matrix


def test_shift_rows_v1():
    EXPECTED = bytearray([0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12, 1, 6, 11])
    data = bytearray(range(16))

    assert from_16x16_matrix(shift_rows(to_16x16_matrix(data))) == EXPECTED

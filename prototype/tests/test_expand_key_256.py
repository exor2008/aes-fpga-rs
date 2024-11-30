from main import KeyType, expand_key


def test_expand_key_256_00():
    # fmt: off
    EXPECTED_KEY = bytearray([
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
        0x62, 0x63, 0x63, 0x63, 0x62, 0x63, 0x63, 0x63, 0x62, 0x63, 0x63, 0x63, 0x62, 0x63, 0x63, 0x63, 
        0xaa, 0xfb, 0xfb, 0xfb, 0xaa, 0xfb, 0xfb, 0xfb, 0xaa, 0xfb, 0xfb, 0xfb, 0xaa, 0xfb, 0xfb, 0xfb, 
        0x6f, 0x6c, 0x6c, 0xcf, 0x0d, 0x0f, 0x0f, 0xac, 0x6f, 0x6c, 0x6c, 0xcf, 0x0d, 0x0f, 0x0f, 0xac, 
        0x7d, 0x8d, 0x8d, 0x6a, 0xd7, 0x76, 0x76, 0x91, 0x7d, 0x8d, 0x8d, 0x6a, 0xd7, 0x76, 0x76, 0x91, 
        0x53, 0x54, 0xed, 0xc1, 0x5e, 0x5b, 0xe2, 0x6d, 0x31, 0x37, 0x8e, 0xa2, 0x3c, 0x38, 0x81, 0x0e, 
        0x96, 0x8a, 0x81, 0xc1, 0x41, 0xfc, 0xf7, 0x50, 0x3c, 0x71, 0x7a, 0x3a, 0xeb, 0x07, 0x0c, 0xab, 
        0x9e, 0xaa, 0x8f, 0x28, 0xc0, 0xf1, 0x6d, 0x45, 0xf1, 0xc6, 0xe3, 0xe7, 0xcd, 0xfe, 0x62, 0xe9, 
        0x2b, 0x31, 0x2b, 0xdf, 0x6a, 0xcd, 0xdc, 0x8f, 0x56, 0xbc, 0xa6, 0xb5, 0xbd, 0xbb, 0xaa, 0x1e, 
        0x64, 0x06, 0xfd, 0x52, 0xa4, 0xf7, 0x90, 0x17, 0x55, 0x31, 0x73, 0xf0, 0x98, 0xcf, 0x11, 0x19, 
        0x6d, 0xbb, 0xa9, 0x0b, 0x07, 0x76, 0x75, 0x84, 0x51, 0xca, 0xd3, 0x31, 0xec, 0x71, 0x79, 0x2f, 
        0xe7, 0xb0, 0xe8, 0x9c, 0x43, 0x47, 0x78, 0x8b, 0x16, 0x76, 0x0b, 0x7b, 0x8e, 0xb9, 0x1a, 0x62, 
        0x74, 0xed, 0x0b, 0xa1, 0x73, 0x9b, 0x7e, 0x25, 0x22, 0x51, 0xad, 0x14, 0xce, 0x20, 0xd4, 0x3b, 
        0x10, 0xf8, 0x0a, 0x17, 0x53, 0xbf, 0x72, 0x9c, 0x45, 0xc9, 0x79, 0xe7, 0xcb, 0x70, 0x63, 0x85,
    ])

    key = bytearray([
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        ] * 15)
    # fmt: on

    expand_key(key, KeyType.K256)

    assert key == EXPECTED_KEY


def test_expand_key_256_ff():
    # fmt: off
    EXPECTED_KEY = bytearray([
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
        0xe8, 0xe9, 0xe9, 0xe9, 0x17, 0x16, 0x16, 0x16, 0xe8, 0xe9, 0xe9, 0xe9, 0x17, 0x16, 0x16, 0x16, 
        0x0f, 0xb8, 0xb8, 0xb8, 0xf0, 0x47, 0x47, 0x47, 0x0f, 0xb8, 0xb8, 0xb8, 0xf0, 0x47, 0x47, 0x47, 
        0x4a, 0x49, 0x49, 0x65, 0x5d, 0x5f, 0x5f, 0x73, 0xb5, 0xb6, 0xb6, 0x9a, 0xa2, 0xa0, 0xa0, 0x8c, 
        0x35, 0x58, 0x58, 0xdc, 0xc5, 0x1f, 0x1f, 0x9b, 0xca, 0xa7, 0xa7, 0x23, 0x3a, 0xe0, 0xe0, 0x64, 
        0xaf, 0xa8, 0x0a, 0xe5, 0xf2, 0xf7, 0x55, 0x96, 0x47, 0x41, 0xe3, 0x0c, 0xe5, 0xe1, 0x43, 0x80, 
        0xec, 0xa0, 0x42, 0x11, 0x29, 0xbf, 0x5d, 0x8a, 0xe3, 0x18, 0xfa, 0xa9, 0xd9, 0xf8, 0x1a, 0xcd, 
        0xe6, 0x0a, 0xb7, 0xd0, 0x14, 0xfd, 0xe2, 0x46, 0x53, 0xbc, 0x01, 0x4a, 0xb6, 0x5d, 0x42, 0xca, 
        0xa2, 0xec, 0x6e, 0x65, 0x8b, 0x53, 0x33, 0xef, 0x68, 0x4b, 0xc9, 0x46, 0xb1, 0xb3, 0xd3, 0x8b, 
        0x9b, 0x6c, 0x8a, 0x18, 0x8f, 0x91, 0x68, 0x5e, 0xdc, 0x2d, 0x69, 0x14, 0x6a, 0x70, 0x2b, 0xde, 
        0xa0, 0xbd, 0x9f, 0x78, 0x2b, 0xee, 0xac, 0x97, 0x43, 0xa5, 0x65, 0xd1, 0xf2, 0x16, 0xb6, 0x5a, 
        0xfc, 0x22, 0x34, 0x91, 0x73, 0xb3, 0x5c, 0xcf, 0xaf, 0x9e, 0x35, 0xdb, 0xc5, 0xee, 0x1e, 0x05, 
        0x06, 0x95, 0xed, 0x13, 0x2d, 0x7b, 0x41, 0x84, 0x6e, 0xde, 0x24, 0x55, 0x9c, 0xc8, 0x92, 0x0f, 
        0x54, 0x6d, 0x42, 0x4f, 0x27, 0xde, 0x1e, 0x80, 0x88, 0x40, 0x2b, 0x5b, 0x4d, 0xae, 0x35, 0x5e,
    ])

    key = bytearray([
        0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
        ] * 15)
    # fmt: on

    expand_key(key, KeyType.K256)

    assert key == EXPECTED_KEY


def test_expand_key_256_v1():
    # fmt: off
    EXPECTED_KEY = bytearray([
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 
        0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f, 
        0xa5, 0x73, 0xc2, 0x9f, 0xa1, 0x76, 0xc4, 0x98, 0xa9, 0x7f, 0xce, 0x93, 0xa5, 0x72, 0xc0, 0x9c, 
        0x16, 0x51, 0xa8, 0xcd, 0x02, 0x44, 0xbe, 0xda, 0x1a, 0x5d, 0xa4, 0xc1, 0x06, 0x40, 0xba, 0xde, 
        0xae, 0x87, 0xdf, 0xf0, 0x0f, 0xf1, 0x1b, 0x68, 0xa6, 0x8e, 0xd5, 0xfb, 0x03, 0xfc, 0x15, 0x67, 
        0x6d, 0xe1, 0xf1, 0x48, 0x6f, 0xa5, 0x4f, 0x92, 0x75, 0xf8, 0xeb, 0x53, 0x73, 0xb8, 0x51, 0x8d, 
        0xc6, 0x56, 0x82, 0x7f, 0xc9, 0xa7, 0x99, 0x17, 0x6f, 0x29, 0x4c, 0xec, 0x6c, 0xd5, 0x59, 0x8b, 
        0x3d, 0xe2, 0x3a, 0x75, 0x52, 0x47, 0x75, 0xe7, 0x27, 0xbf, 0x9e, 0xb4, 0x54, 0x07, 0xcf, 0x39, 
        0x0b, 0xdc, 0x90, 0x5f, 0xc2, 0x7b, 0x09, 0x48, 0xad, 0x52, 0x45, 0xa4, 0xc1, 0x87, 0x1c, 0x2f, 
        0x45, 0xf5, 0xa6, 0x60, 0x17, 0xb2, 0xd3, 0x87, 0x30, 0x0d, 0x4d, 0x33, 0x64, 0x0a, 0x82, 0x0a, 
        0x7c, 0xcf, 0xf7, 0x1c, 0xbe, 0xb4, 0xfe, 0x54, 0x13, 0xe6, 0xbb, 0xf0, 0xd2, 0x61, 0xa7, 0xdf, 
        0xf0, 0x1a, 0xfa, 0xfe, 0xe7, 0xa8, 0x29, 0x79, 0xd7, 0xa5, 0x64, 0x4a, 0xb3, 0xaf, 0xe6, 0x40, 
        0x25, 0x41, 0xfe, 0x71, 0x9b, 0xf5, 0x00, 0x25, 0x88, 0x13, 0xbb, 0xd5, 0x5a, 0x72, 0x1c, 0x0a, 
        0x4e, 0x5a, 0x66, 0x99, 0xa9, 0xf2, 0x4f, 0xe0, 0x7e, 0x57, 0x2b, 0xaa, 0xcd, 0xf8, 0xcd, 0xea, 
        0x24, 0xfc, 0x79, 0xcc, 0xbf, 0x09, 0x79, 0xe9, 0x37, 0x1a, 0xc2, 0x3c, 0x6d, 0x68, 0xde, 0x36,
    ])

    key = bytearray([
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
        0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f,
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
        0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f,
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
        0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f,
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
        0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f,
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
        0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f,
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
        0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f,
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
        0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f,
        0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f,
    ])
    # fmt: on

    expand_key(key, KeyType.K256)

    assert key == EXPECTED_KEY
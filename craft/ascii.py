import unittest


def run():
    print(ascii_list())
    unittest.main()


def ascii_list(start=32, end=127):
    ascii = ""

    if not ((start < end) and (32 <= start) and (end <= 127)):
        raise ValueError

    for i in range(start, end):
        ascii += chr(i)
    return ascii


class TestASCII(unittest.TestCase):
    def test_ascii(self):
        self.assertEqual(
            ascii_list(),
            " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~",
        )


if __name__ == "__main__":
    run()

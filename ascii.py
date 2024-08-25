import unittest


def run():
    print(ascii_list())
    unittest.main()


def alpha():
    for i in all:
        if i.isalpha():
            print(i, end="")


def ascii_list(start=32, end=127):
    ascii_string = ""

    if not ((start < end) and (32 <= start) and (end <= 127)):
        raise ValueError

    for i in range(start, end):
        ascii_string += chr(i)
    return ascii_string


def TestASCII(TestCase):
    def test_valid(self):
        self.assertEqual(
            ascii_list(),
            " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~",
        )


if __name__ == "__main__":
    run()

def run():
    '''print()
    for i in ascii_meta():
        print(i)'''
    
    print()
    for i in ascii_list():
        print(i, end="")


def ascii_list(start=32, end=127):
    ascii = []

    if not((start < end) and (32 <= start) and (end <= 127)):
        raise ValueError
    
    for i in range(start, end):
        ascii.append(chr(i))
    return ascii


def ascii_meta(start=32, end=127):
    map = {}
    meta_list = []

    if not((start < end) and (32 <= start) and (end <= 127)):
        raise ValueError
    
    for i in range(start, end):
        map[str(i).zfill(3)] = chr(i)

    for key, value in map.items():
        b = str(bin(int(key))).replace("0b", "").zfill(8)
        text = b + key + " = " + value
        meta_list.append(text)

    return meta_list


if __name__ == "__main__":
    run()

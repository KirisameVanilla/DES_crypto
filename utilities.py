def bit_to_str(bits):
    result = ''
    groups = int(len(bits) / 8)
    for i in range(groups):
        cur_bits = bits[i * 8:i * 8 + 8:1]
        while cur_bits[0] == '0':
            cur_bits = cur_bits[1:]
            if len(cur_bits) == 0:
                break
        if len(cur_bits) == 0:
            continue
        cur_asc = int(cur_bits, 2)
        cur_asc = chr(cur_asc)
        result = result + cur_asc
    return result


def str_to_bit(content):
    bits = ''
    for i in content:
        asc2i = bin(ord(i))[2:]
        asc2i = asc2i.rjust(8, '0')
        bits = bits + asc2i
    return bits


def read_file(filename):
    try:
        fp = open(filename, 'r', encoding='utf-8')
        content = fp.read()
        fp.close()
        return content
    except IOError:
        print("Open file failed!")
        return False


def write_file(path, content):
    try:
        file = open(f'{path}', 'w', encoding='utf-8')
        file.write(content)
        file.close()
        return True
    except IOError:
        print("Error")
        return False

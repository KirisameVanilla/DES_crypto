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
        print("Read failed!")
        return False


def write_file(path, content):
    try:
        file = open(f'{path}', 'w', encoding='utf-8')
        file.write(content)
        file.close()
        return True
    except IOError:
        print("Write failed")
        return False


def xor(text_1, text_2) -> str:
    # 异或
    length = len(text_1)
    result = ''
    for i in range(length):
        if text_1[i] == text_2[i]:
            result = result + '0'
        else:
            result = result + '1'
    return result


def permutation(origin_text, permutation_table) -> str:
    # 用于位置换运算
    result_text = ''
    for i in permutation_table:
        result_text = result_text + origin_text[int(i) - 1]
    return result_text


def divide(origin) -> tuple[str, str]:
    total_length = len(origin)
    half_length = int(total_length / 2)
    L = origin[0:half_length:1]
    R = origin[half_length:total_length:1]
    return L, R


def calc_IP_Decrypt_table(IP_table) -> list:
    # For users to personalize their IP_table
    index_mapping = {value: index for index, value in enumerate(IP_table, start=1)}
    ip_inverse_table = [index_mapping[i] for i in range(1, len(IP_table) + 1)]
    return ip_inverse_table

import random


def permutation(origin_text, permutation_table) -> str:
    # 用于位置换运算
    result_text = ''
    for i in permutation_table:
        result_text = result_text + origin_text[int(i) - 1]
    return result_text


def IP_Cipher(plaintext) -> str:
    # IP置换
    ip_table = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    IP_text = permutation(plaintext, ip_table)
    return IP_text


def IP_Decipher(IP_text) -> str:
    # 逆IP置换
    de_ip_table = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]
    plaintext = permutation(IP_text, de_ip_table)
    return plaintext


def divide(key_origin) -> tuple[str, str]:
    total_length = len(key_origin)
    half_length = int(total_length / 2)
    L = key_origin[0:half_length:1]
    R = key_origin[half_length:total_length:1]
    return L, R


def PC_1_Cipher(plaintext) -> str:
    # PC-1置换，会自动去除校验位
    pc_1_table = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]
    PC_1_text = permutation(plaintext, pc_1_table)
    return PC_1_text


def PC_2_Cipher(plaintext) -> str:
    # PC-2置换
    pc_2_table = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
    ]
    PC_2_text = permutation(plaintext, pc_2_table)
    return PC_2_text


def left_move(text) -> str:
    new_text = text[1:]
    new_text = new_text + text[0]
    return new_text


def get_K(key_origin) -> list:
    # 得到16个密钥K

    # 循环左移表
    left_move_table = [0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    C0, D0 = divide(key_origin)
    C_list = [C0]
    D_list = [D0]
    CD_list = []
    K_list = []
    for i in range(16):
        C = C_list[i]
        D = D_list[i]
        i = i + 1
        left_move_times = left_move_table[i]
        while left_move_times > 0:
            C = left_move(C)
            D = left_move(D)
            left_move_times = left_move_times - 1
        C_list.append(C)
        D_list.append(D)
    for i in range(16):
        i = i + 1
        CD = C_list[i] + D_list[i]
        CD_list.append(CD)
    for elem in CD_list:
        K = PC_2_Cipher(elem)
        K_list.append(K)
    return K_list


def create_random_binary_int() -> str:
    random_num = random.randint(0, pow(2, 56) - 1)
    binary_num = bin(random_num)
    binary_str = str(binary_num)[2:].zfill(56)
    return binary_str


def add_odd_check(binary_str) -> str:
    binary_str_odd_check = ''
    for i in range(8):
        start_index = i * 7
        end_index = (i + 1) * 7
        binary_str_odd_check = binary_str_odd_check + binary_str[start_index:end_index:1]
        bit_sum = 0
        for bit in binary_str[start_index:end_index:1]:
            bit_sum += int(bit)
        if bit_sum % 2 == 0:
            checksum = '1'
        else:
            checksum = '0'
        binary_str_odd_check = binary_str_odd_check + checksum[0]
    return binary_str_odd_check


def del_odd_check(binary_str_odd_check) -> str:
    binary_str = ''
    for i in range(8):
        start_index = i * 8
        end_index = (i + 1) * 8
        binary_str = binary_str + binary_str_odd_check[start_index:end_index - 1:1]
    return binary_str


def extend(text) -> str:
    # 扩展置换
    extend_table = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1
    ]
    extend_text = permutation(text, extend_table)
    return extend_text


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


def S_change(text_48) -> str:
    # S盒转换
    texts = []
    S_texts = ''
    for i in range(8):
        text = text_48[i * 6:i * 6 + 6:1]
        texts.append(text)
    S_table = [
        14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
        0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
        4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
        15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
    ]
    for text in texts:
        i = int(text[0] + text[-1], 2)
        j = int(text[1:-1], 2)
        index = i * 16 + j - 1
        S_text = S_table[index]
        S_text = bin(S_text)[2:].rjust(4, '0')
        S_texts = S_texts + S_text
    return S_texts


def P_Cipher(plaintext) -> str:
    # P盒置换
    P_table = [
        16, 7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        2, 8, 24, 14,
        32, 27, 3, 9,
        19, 13, 30, 6,
        22, 11, 4, 25
    ]
    P_text = permutation(plaintext, P_table)
    return P_text


def wheel(M0, K_list) -> str:
    # 轮运算
    L0, R0 = divide(M0)
    L_list = [L0]
    R_list = [R0]
    for i in range(16):
        R = R_list[i]
        L = L_list[i]
        R_1 = extend(R)
        R_2 = xor(R_1, K_list[i])
        R_3 = S_change(R_2)
        R_4 = P_Cipher(R_3)
        R_new = xor(L, R_4)
        R_list.append(R_new)
        L_list.append(R)
    M16 = R_list[-1] + L_list[-1]
    M_final = IP_Decipher(M16)
    return M_final


def encrypt(bits) -> tuple[str, str]:
    key_56 = create_random_binary_int()
    key_64 = add_odd_check(key_56)
    # 先对密钥K进行PC-1置换
    K_PC_1 = PC_1_Cipher(key_64)
    K_list = get_K(K_PC_1)
    bits_list = []
    length = len(bits)
    # 计算要把比特流分为几个组分别进行同密钥的加密
    groups = int(length / 64)
    result = ''
    if groups * 64 < length:
        groups += 1
        bits = bits.ljust(groups * 64, '0')
    for group in range(groups):
        bits_list.append(bits[group * 64:group * 64 + 64:1])
    for each_bits in bits_list:
        each_bits = IP_Cipher(each_bits)
        M_final = wheel(each_bits, K_list)
        M_hex = hex(int(M_final, 2))[2:]
        result = result + M_hex
    return result, key_64

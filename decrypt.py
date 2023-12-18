from encrypt import IP_Decipher, IP_Cipher, divide, PC_1_Cipher, get_K, extend, xor, S_change, P_Cipher


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


def decrypt(encrypted_text, key):
    M16 = IP_Cipher(encrypted_text)
    R16, L16 = divide(M16)
    R_list = [R16]
    L_list = [L16]
    K_PC_1 = PC_1_Cipher(key)
    K_list = get_K(K_PC_1)
    for wheel_times in range(16):
        cur_R = R_list[wheel_times]
        key_serial = 16 - wheel_times - 1
        R_new = L_list[wheel_times]
        R_1 = extend(R_new)
        R_2 = xor(R_1, K_list[key_serial])
        R_3 = S_change(R_2)
        R_4 = P_Cipher(R_3)
        L_new = xor(R_4, cur_R)
        L_list.append(L_new)
        R_list.append(R_new)
    M0 = L_list[16] + R_list[16]
    M = IP_Decipher(M0)
    print(bit_to_str(M))
    return bit_to_str(M)

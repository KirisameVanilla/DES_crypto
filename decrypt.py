from encrypt import IP_Decipher, IP_Cipher, PC_1_Cipher, get_K, extend, S_change, P_Cipher
from utilities import xor, divide


def decrypt(encrypted_text, key):
    groups = int(len(encrypted_text) / 16)
    decrypted_message = ''
    for i in range(groups):
        cur_hex = encrypted_text[i * 16:i * 16 + 16:1]
        cur_int = int(cur_hex, 16)
        cur_bits = bin(cur_int)[2:].rjust(64, '0')
        M16 = IP_Cipher(cur_bits)
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
        decrypted_message = decrypted_message + M
    return decrypted_message

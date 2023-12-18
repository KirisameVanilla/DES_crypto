import tkinter as tk
from tkinter import filedialog
from encrypt import encrypt
from decrypt import decrypt


def read_file(filename):
    try:
        fp = open(filename, 'r', encoding='utf-8')
        content = fp.read()
        fp.close()
        return content
    except IOError:
        print("Open file failed!")
        return False


def str_to_bit(content):
    bits = ''
    for i in content:
        asc2i = bin(ord(i))[2:]
        asc2i = asc2i.rjust(8, '0')
        bits = bits + asc2i
    return bits


def write_file(path, content, name):
    try:
        file = open(f'{path}\\{name}.txt', 'w', encoding='utf-8')
        file.write(content)
        file.close()
        return True
    except IOError:
        print("Error")
        return False


def encrypt_part():
    filename = filedialog.askopenfilename(title="请选择要加密的文件", filetypes=[("所有文件", "*.*")])
    save_path = filedialog.askdirectory(title="请选择保存加密文件以及密钥的位置")
    message = read_file(filename)
    bits = str_to_bit(message)
    DES_text, key = encrypt(bits)
    write_file(save_path, DES_text, 'encrypted')
    write_file(save_path, key, 'key')
    return DES_text, key


def decrypt_part():
    encrypted_filename = filedialog.askopenfilename(title="请选择要解密的文件", filetypes=[("所有文件", "*.*")])
    key_filename = filedialog.askopenfilename(title="请选择密钥", filetypes=[("文本文件", "*.txt")])
    save_path = filedialog.askdirectory(title="请选择保存解密内容的位置")
    encrypted_message = read_file(encrypted_filename)
    key_message = read_file(key_filename)
    groups = int(len(encrypted_message) / 16)
    decrypted_message = ''
    for i in range(groups):
        cur_hex = encrypted_message[i * 16:i * 16 + 16:1]
        cur_int = int(cur_hex, 16)
        cur_bits = bin(cur_int)[2:].rjust(64, '0')
        decrypted_message = decrypted_message + decrypt(cur_bits, key_message)
    write_file(save_path, decrypted_message, 'decrypted')
    return decrypted_message


if __name__ == '__main__':
    root = tk.Tk()
    root.title("文件加密解密")
    button_fun1 = tk.Button(root, text="加密", command=encrypt_part)
    button_fun1.pack(pady=10)
    button_fun2 = tk.Button(root, text="解密", command=decrypt_part)
    button_fun2.pack(pady=10)
    root.mainloop()

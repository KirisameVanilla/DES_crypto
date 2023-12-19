import tkinter as tk
from tkinter import filedialog
from encrypt import encrypt
from decrypt import decrypt
from utilities import read_file, write_file, str_to_bit, bit_to_str


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
    decrypted_message = decrypt(encrypted_message, key_message)
    decrypted_message = bit_to_str(decrypted_message)
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

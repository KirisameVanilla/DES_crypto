import tkinter as tk
from tkinter import filedialog
from encrypt import encrypt
from decrypt import decrypt
from utilities import read_file, write_file, str_to_bit, bit_to_str


def encrypt_part():
    filename = filedialog.askopenfilename(title="请选择要加密的文件", filetypes=[("文本文件", "*.txt")])
    encrypted_save_path = filedialog.asksaveasfilename(title="加密文件另存为", filetypes=[("文本文件", "*.txt")]) + ".txt"
    key_save_path = filedialog.asksaveasfilename(title="密钥另存为", filetypes=[("文本文件", "*.txt")]) + ".txt"
    message = read_file(filename)
    bits = str_to_bit(message)
    DES_text, key = encrypt(bits)
    write_file(encrypted_save_path, DES_text)
    write_file(key_save_path, key)
    return DES_text, key


def decrypt_part():
    encrypted_filename = filedialog.askopenfilename(title="请选择要解密的文件", filetypes=[("文本文件", "*.txt")])
    key_filename = filedialog.askopenfilename(title="请选择密钥", filetypes=[("文本文件", "*.txt")])
    save_path = filedialog.asksaveasfilename(title="解密内容另存为", filetypes=[("文本文件", "*.txt")]) + ".txt"
    encrypted_message = read_file(encrypted_filename)
    key_message = read_file(key_filename)
    decrypted_message = decrypt(encrypted_message, key_message)
    decrypted_message = bit_to_str(decrypted_message)
    write_file(save_path, decrypted_message)
    return decrypted_message


if __name__ == '__main__':
    root = tk.Tk()
    root.title("文件加密解密")
    button_fun1 = tk.Button(root, text="加密", command=encrypt_part)
    button_fun1.pack(pady=10)
    button_fun2 = tk.Button(root, text="解密", command=decrypt_part)
    button_fun2.pack(pady=10)
    root.mainloop()

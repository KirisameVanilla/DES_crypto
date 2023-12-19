import tkinter as tk
from tkinter import filedialog, font
from encrypt import encrypt
from decrypt import decrypt
from utilities import read_file, write_file, str_to_bit, bit_to_str
from PIL import Image, ImageTk


def set_background_image(Canvas):
    path = 'res/python_logo.png'
    image = Image.open(f"{path}")
    image_tk = ImageTk.PhotoImage(image)
    Canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
    # 保持对ImageTk对象的引用，以避免被垃圾回收
    Canvas.image = image_tk


def open_new_window(name, text):
    # 创建新窗口
    new_window = tk.Toplevel(root)
    new_window.title(f"{name}")

    # 在新窗口中显示文字
    label_text = tk.Label(new_window, text=f"{text}")
    label_text.pack(padx=20, pady=20)


def encrypt_part():
    filename = filedialog.askopenfilename(title="请选择要加密的文件", filetypes=[("文本文件", "*.txt")])
    encrypted_save_path = filedialog.asksaveasfilename(title="加密文件另存为",
                                                       filetypes=[("文本文件", "*.txt")]) + ".txt"
    key_save_path = filedialog.asksaveasfilename(title="密钥另存为", filetypes=[("文本文件", "*.txt")]) + ".txt"
    message = read_file(filename)
    bits = str_to_bit(message)
    DES_text, key = encrypt(bits)
    write_file(encrypted_save_path, DES_text)
    write_file(key_save_path, key)
    open_new_window('Window', 'Encrypt Finished!')
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
    open_new_window('Window', 'Decrypt Finished!')
    return decrypted_message


if __name__ == '__main__':
    width = height = 600
    geometry_string = f"{width}x{height}"
    root = tk.Tk()
    root.geometry(geometry_string)

    root.title("文件加密解密")
    canvas = tk.Canvas(root, width=600, height=600)
    canvas.pack()
    set_background_image(canvas)

    font = font.Font(family='Times', size=16, weight='bold')
    button_fun1 = tk.Button(canvas, text="Encrypt", command=encrypt_part, width=25, height=10, font=font)
    canvas.create_window(150, 0, anchor=tk.NW, window=button_fun1)
    button_fun2 = tk.Button(canvas, text="Decrypt", command=decrypt_part, width=25, height=10, font=font)
    canvas.create_window(150, 300, anchor=tk.NW, window=button_fun2)
    root.mainloop()

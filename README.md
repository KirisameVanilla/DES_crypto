# 项目技术文档

## 项目简介
本文档包含了一个基于 DES 加密算法的文件加密解密应用程序的四个 Python 文件的详细说明。这个应用程序通过 Tkinter 创建图形用户界面（GUI），并使用文件对话框选择要处理的文件。

## 项目结构
project/  
|-- main.py  
|-- encrypt.py  
|-- decrypt.py  
|-- utilities.py  
|-- README.md  
|-- .gitignore  
|-- res/background_image.png

## encrypt.py

### 模块说明
本模块包含了一个基于DES原理的加密算法。该算法实现了IP置换、逆IP置换、PC-1置换、PC-2置换、循环左移、生成16个子密钥、扩展置换、S盒转换、P盒置换以及轮运算。

### 函数和方法
`IP_Cipher(plaintext) -> str`

描述: 执行IP置换。  
参数:   
plaintext (str): 64位二进制明文。  
返回:   
IP_text (str): IP置换后的文本。

`IP_Decipher(IP_text) -> str`

描述: 执行逆IP置换。  
参数:   
IP_text (str): 经过IP置换的文本。  
返回:   
plaintext (str): 逆IP置换后的文本。

`PC_1_Cipher(plaintext) -> str`

描述: 执行PC-1置换，自动去除校验位。  
参数:   
plaintext (str): 64位二进制文本。  
返回:   
PC_1_text (str): PC-1置换后的文本。

`PC_2_Cipher(plaintext) -> str`

描述: 执行PC-2置换。  
参数:   
plaintext (str): 56位二进制文本。  
返回:   
PC_2_text (str): PC-2置换后的文本。

`left_move(text) -> str`

描述: 执行循环左移操作。  
参数:   
text (str): 待移位的文本。  
返回:   
new_text (str): 循环左移后的文本。

`get_K(key_origin) -> list`

描述: 生成16个子密钥。  
参数:   
key_origin (str): 64位二进制原始密钥。  
返回:   
K_list (list): 包含16个子密钥的列表。

`create_random_binary_int() -> str`

描述: 生成56位随机二进制数。  
返回:   
binary_str (str): 56位二进制随机数。

`add_odd_check(binary_str) -> str`

描述: 添加奇偶校验位。  
参数:   
binary_str (str): 56位二进制数。  
返回:   
binary_str_odd_check (str): 带奇偶校验位的二进制数。

`del_odd_check(binary_str_odd_check) -> str`

描述: 删除奇偶校验位。  
参数:   
binary_str_odd_check (str): 带奇偶校验位的二进制数。  
返回:   
binary_str (str): 不带奇偶校验位的二进制数。

`extend(text) -> str`

描述: 执行扩展置换。  
参数:   
text (str): 32位二进制文本。  
返回:   
extend_text (str): 扩展置换后的文本。

`S_change(text_48) -> str`

描述: 执行S盒转换。  
参数:   
text_48 (str): 48位二进制文本。  
返回:   
S_texts (str): S盒转换后的文本。

`P_Cipher(plaintext) -> str`

描述: 执行P盒置换。  
参数:   
plaintext (str): 32位二进制文本。  
返回:   
P_text (str): P盒置换后的文本。

`wheel(M0, K_list) -> str`

描述: 执行轮运算。  
参数:   
M0 (str): 64位二进制明文。  
K_list (list): 包含16个子密钥的列表。  
返回:   
M_final (str): 轮运算后的文本。

`encrypt(bits) -> tuple[str, str]`

描述: 对输入比特流进行加密。  
参数:   
bits (str): 待加密的比特流。  
返回:   
(result, key_64) (tuple): 加密结果和使用的64位密钥。

## decrypt.py

### 模块说明
本模块包含了一个基于DES原理的解密算法。该算法实现了逆轮运算。

### 函数和方法
`decrypt(encrypted_text, key) -> str`

描述: 执行解密操作。  
参数:   
encrypted_text (str): 加密后的文本。  
key (str): 密钥。  
返回:   
decrypted_message (str): 解密后的明文。

## utilities.py

### 模块说明
本模块包含了一组用于处理比特流、字符串和文件的实用函数。

### 函数和方法
`bit_to_str(bits) -> str`

描述: 将比特流转换为字符串。  
参数:   
bits (str): 要转换的比特流。  
返回:   
result (str): 转换后的字符串。

`str_to_bit(content) -> str`

描述: 将字符串转换为比特流。  
参数:   
content (str): 要转换的字符串。  
返回:   
bits (str): 转换后的比特流。

`read_file(filename) -> str`

描述: 读取文件内容。  
参数:  
filename (str): 文件的绝对地址。  
返回:  
content (str): 文件的内容(若成功读取文件)  
False (bool): (若读取文件失败)

`write_file(path, content) -> bool`

描述: 将内容写入文件。  
参数:  
path (str): 文件的绝对地址。  
content (str): 需要写入的内容。  
返回:  
True (bool): (若成功写入文件)  
False (bool): (若写入文件失败)

`xor(text_1, text_2) -> str`

描述: 执行异或操作。  
参数:  
text_1 (str): 进行异或操作的第一个比特字符串。  
text_2 (str): 进行异或操作的第一个比特字符串。  
返回:  
result (str): 进行异或操作得到的结果字符串。

`permutation(origin_text, permutation_table) -> str`

描述: 用于位置换运算。  
参数:  
origin_text (str): 进行位置换操作的字符串。  
permutation_table (list): 位置换加密表。  
返回：  
result_text (str): 位置换加密操作得到的字符串。

`divide(origin) -> tuple[str, str]`

描述: 将比特流分为两半。  
参数:  
origin (str): 需要进行拆分的字符串。  
返回:  
(L, R) (tuple): 拆分后的左右字符串。

`calc_IP_Decrypt_table(IP_table) -> list`

描述: 计算逆IP置换表。  
参数:  
IP_table (list): 需要计算逆操作表的原IP表。  
返回:  
ip_inverse_table (list): 逆IP置换表。

## main.py

### 模块说明
本模块包含了基于 Tkinter 构建的 GUI 应用程序，调用encrypt.py以及decrypt.py进行加密解密操作，是本项目的程序入口。

### 函数与方法
`set_background_image(Canvas)`

描述: 设置 GUI 的背景图像。  
参数:  
Canvas (tk.Canvas): 画布对象。

`open_new_window(name, text)`

描述: 在新窗口中显示文本。  
参数:  
name (str): 窗口标题。  
text (str): 要显示的文本。

`encrypt_part()`

描述: 处理加密操作。弹出文件对话框选择要加密的文件，并保存加密后的内容和密钥。

`decrypt_part()`

描述: 处理解密操作。弹出文件对话框选择要解密的文件和密钥文件，并保存解密后的内容。

`main()`

描述: 主程序入口。创建 GUI 窗口，设置背景图像，添加 Encrypt 和 Decrypt 按钮，启动 GUI 主循环。
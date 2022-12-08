# 打开并读取文件，内容显示到屏幕
with open('file.txt') as file_object:
    contents = file_object.read()
    print(contents)
    # 删除行末尾空白
    print(contents.rstrip())

# 路径,windows用双反斜杠'\\'
with open('C:\\Users\\sunxi\Desktop\\EmimOH.mmol') as file_objects2:
    contents2 = file_objects2.read()
    print(contents2.rstrip())

# # 绝对路径存储在一个变量中，将变量传递给open
file_path = 'C:\\Users\\sunxi\\Desktop\\Emim.txt'
with open(file_path) as file_objects3:
    contents3 = file_objects3.read()
    print(contents3.rstrip())

# 逐行读：对文件对象使用for循环
filename = '.\\file.txt'
with open(filename) as file_objcet4:
    for line in file_objcet4:
        # 逐行读，消除每行空白
        print(line.rstrip())

# 创建一个包含文件各行列表
# 在with代码块外使用文件内容，将文件的各行存储在一个列表中，再在with代码块外打印
# readlines()从文件中读取每一行，并将其存储在一个列表中；接下来，列表被存储在变量lines中
filename2 = '.\\file.txt'
with open(filename2) as file_object5:
    lines = file_object5.readlines()
    for line in lines:
        print(line.rstrip())


# 使用文件内容
cont = ''
for line in lines:
    cont += line.rstrip()   # 删除一行右面空格
    print(cont.strip())   # 删除一行左面空格
    print(cont[:52])    # 打印前52个字符
    print(len(cont))   # 打印字符串长度
# 注意：读取文本文件时，Python将所有文本读为字符串
# 如果你读取数字作为数值使用，必须用int() 转换为整数，或用float() 转换为浮点数

# 写入空文件
# 将内容写入文件，需要给open了另一个参数，告诉内容写入另一文件
# 读取'r'、写入'w'、附加'a'、读取和写入文件'r+'

filename = '.\\programming.txt'
with open(filename, 'w') as file_object:
    file_object.write('I love you forever!')

# 注意：Python只能将字符串写入文件，将数值数据存储到文本中，必须先用str() 转为字符串格式

# 写入多行
filename2='programming2.txt'
with open(filename2,'w') as file_object2:
    file_object2.write('I am xysun!\n')
    file_object2.write('I am a girl!\n')

# 附加到文件
with open(filename2,'a') as file_object3:
    file_object3.write('I am 23!')

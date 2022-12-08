# 读取文件练习
# 判断一个文件里是否有我的生日
filename = '.\\file.txt'
cont = ''
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        cont += line.rstrip()
brithday = input('Entry your brithday,in the form mmddyy:')
if brithday in cont:
    print("your brithday is in the data!")
else:
    print("your brithday is not in the data..")

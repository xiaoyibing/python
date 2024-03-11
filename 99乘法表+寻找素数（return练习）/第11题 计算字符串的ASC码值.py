#从键盘上输入一个纯英文字符串（大写字母小写字母都有），
#计算出各个字符的ASC码值之和。
q=input('请输入字符串：')
n=0
for i in q:
    a=ord(i)
    n+=a
print(n) 

#从键盘上输入一个4位数，比如3589，求各位数之和，即3+5+8+9之和，结果为25
num='3589'
add=0
for i in num:
    a=int(i)
    add+=a
print(add)

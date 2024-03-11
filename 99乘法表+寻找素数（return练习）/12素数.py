#从键盘上输入一个整数，要求判断其是否为素数

def sss(num):
    n=0
    for i in range(2,num):
        if num%i==0:
            n+=1
            break
    if n==0:
        print('是素数')
    else:
        print('不是素数')
while(1):
    num=int(input('请输入数字：'))
    sss(num)
            
            

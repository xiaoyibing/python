'''任务2：在任务1基础上，继续编程实现简版收银台：
1）员工输入员工码、密码和验证码进入系统，
2）支持同种商品数量合并，
3）重复收银(提示金额)，显示小票（小票格式尽量仿超市真实小票） 
要求有主菜单：1--录入商品，2--商品扫码查询，3--收银，4--退出 
要求收银为扫付款码，能识别付款码的特征符'''
# -----欢迎语-----
import random
print('欢迎使用小超市商品录入与查询系统！')
#------数据库-----
#一定要在二维码上加引号
ls=[['9787560855295','高数第3版课本',36.00],\
    ['6921168520015','1.5L农夫山泉矿泉水',3.00],\
    ['6922868283446','99.9%杀菌湿巾',4.00],\
    ['6973870130341','1L乳酸菌饮料',4.00],\
    ['6953787302420','一支笔笔芯 20支/盒',10.00]]
ls1=[]
#随机验证码
yzm=random.randint(16411,234364)
# 建立字典
a={}
# 将数据库中的数据加入到字典a中
for i in range(len(ls)):
    name=ls[i][1]
    number=ls[i][0]
    money=ls[i][2]
    a[number]=[name,money]
#----------主程序——
# 验证身份
print('默认密码：123')
xingming=input('请输入员工码：')
mima=input('请输入密码：')
print('验证码已发送:')
print(yzm)
yanzhengma=int(input('请输入验证码：'))
if mima == '123' and yanzhengma == yzm :
    print('\n')
    print('这是原有数据库：')
    print(a)
    print('\n')
    print('请选择您需要的功能：')
    while (1):
        q = int(input("1--录入商品    2--商品扫码查询  3--收银   4--退出"))
        if q == 1:
            print('正在启动录入商品...')
            name = input('请录入商品名称：')
            number = input("请录入商品条码号：")
            money = input('请录入商品单价：')
            a[number] = [name, money]
        if q == 2:
            print('现在进行的是  商品扫码查询')
            number = input('请扫码：')
            print(f"该商品的名称是：{a[number][0]}")
            print(f"该商品的单价是：{a[number][1]}")
        if q == 3:
            all_money = 0
            c = 1
            while (1):
                if c == 1:
                    number = input('扫码：')
                    all_money += a[number][1]
                    print(f'{a[number][0]}*1')
                    print(f'目前商品金额为：{all_money}元')
                    ls1.append(a[number][0])
                    c = int(input('是否继续扫码  1.继续   2.停止并结算'))
                    print(ls1)
                if c == 2:
                    #合计数目
                    d = {}
                    for i in ls1:
                        print(i)
                        d[i] = ls1.count(i)
                    print('------------------小票--------------------')
                    print('商品清单如下：')
                    for i in d:
                        print(f'{i}*{d[i]}')
                    print(f'商品总价为：{all_money}元')
                    break
        if q == 4:
            print("已退出")
            break
else:
    print("员工码，密码，或验证码错误")

#扫雷（文字版）

import random

n=0#记录已展开的个数，若达到90个（有十个雷），则宣布胜利
class Mine:
    def __init__(self):
        self.write_face = '■'#显现在表面的值
        self.write_in = '□'#显现在内部的值
    def click(self):
        global n
        self.write_face=self.write_in#当点击它时，内部的值将浮于表面
        n+=1#展开个数加一


#表面装■，内部装□
mains = [[0 for _ in range(10)] for _ in range(10)]#设置一个10*10列表
for i in range(10):
    for j in range(10):
        mains[i][j] = Mine()#将列表与Mine类联系起来
#装雷---将内部的□，换成*
num_lie = 0
while num_lie < 10:
    x, y = random.randint(0, 9), random.randint(0, 9)#随机抽取坐标
    if mains[x][y].write_in != ' *':#判断之前没有抽取过
        mains[x][y].write_in = ' *'
        num_lie += 1
#装雷数-----将非雷换成周围的雷数
for i in range(10):
    for j in range(10):
        if mains[i][j].write_in != ' *':#判断非雷
            nn= 0
            for a in range(-1,2):
                for b in range(-1,2):
                    if (0 <= i - a <= 9) and (0 <= j - b <= 9):
                        if mains[i - a][j - b].write_in == ' *':
                            nn += 1
            mains[i][j].write_in =' '+str(nn)#将□换成周围雷数
def lian(x,y):#使周围雷个数为0的周围展开
    if mains[x][y].write_in==' 0':#判断周围无雷
        for i in range(-1,2):
            for j in range(-1,2):
                if (0 <= x-i <= 9) and (0 <= y-j <= 9):
                    #判断之前没展开过（表面不等于内部，就是没展开的）
                    if mains[x-i][y-j].write_in != ' *' and mains[x-i][y-j].write_in!=mains[x-i][y-j].write_face:
                        mains[x-i][y-j].click()
                        lian(x-i,y-j)#递归
def face():
    #显示face
    print(' ', end='')
    for i in range(10):
        print(' '+str(i), end='')
    print()
    for i in range(10):
        print(i, end='')
        for j in range(10):
            print(mains[i][j].write_face, end='')
        print()
def iin():#显示内部
    print(' ', end='')
    for i in range(10):
        print(' '+str(i), end='')
    print()
    for i in range(10):
        print(i, end='')
        for j in range(10):
            print(mains[i][j].write_in, end='')
        print()
    print('\n')
#--循环----------------
                     
while(1):
    iin()
    face()
    #输入点击
    xy=input('请输入行数和列数（如：22）:')
    mains[int(xy[1])][int(xy[0])].click()
    lian(int(xy[1]),int(xy[0]))
    if mains[int(xy[1])][int(xy[0])].write_in==' *':#判断是否踩到雷
        iin()
        print('Game Over!')
        break
    if n==90:#判断是否胜利
        iin()
        print('胜利！')
        break


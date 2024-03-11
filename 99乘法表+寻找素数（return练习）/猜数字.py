'''编程1：你想我猜
电脑产生一个[1-99]的随机整数，让我们来猜，每猜一次后电脑会提示你猜的数是大了还是小了，最多
可以猜9次，如果还未猜中，电脑会说“游戏结束，你没猜中，真笨啊！”，如果你是5次以内（含5次）就
猜中了，电脑提示出很好评价，如果你是6-7次或8-9次猜中，电脑的评价都不一样（共3类评价）。游戏
支持玩家再玩一次。
'''
import random
qq='y'
while(qq=='y'):
    number=random.randint(1,100)
    print(number)
    n=1
    while(n<=9):
        an=int(input('请输入你猜测的数字：'))
        if an==number:
            if n<=5:
                print(f'恭喜你猜对了！已战胜当前80%的用户。共猜了{n}次。')
                n+=1
                break
            if 6<=n<=7:
                print(f'恭喜你猜对了！已战胜当前60%的用户。共猜了{n}次。')
                n+=1
                break
            if 8<=n<=9:
                print(f'恭喜你猜对了！已战胜当前40%的用户。共猜了{n}次。')
                n+=1
                break
        if an!=number:
            if an>=number:
                print('大了')
            if an<=number:
                print('小了')
            n+=1
    if n>=10:
        print('都猜错了呢！')
    qq=input('是否再玩一次？  y/n')
    

        
                  

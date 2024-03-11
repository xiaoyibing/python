#求3-8位的水仙花数，能重玩
'''一位自幂数：独身数
三位自幂数：水仙花数
四位自幂数：四叶玫瑰数
五位自幂数：五角星数
六位自幂数：六合数
七位自幂数：北斗七星数
八位自幂数：八仙数
九位自幂数：九九重阳数
十位自幂数：十全十美数'''
while(True):
    q = int(input("请输入您想要求的水仙花数的位数(3~8)："))
    if q==3:
        for a in range(1, 10):
            for b in range(10):
                for c in range(10):
                    if (a ** 3 + b ** 3 + c ** 3 == a * 100 + b * 10 + c):
                        print(f"{a}{b}{c}")
    if q==4:
        for a in range(1,10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        if (a ** 4 + b ** 4 + c ** 4+d**4 == a * 1000 + b * 100 + c*10+d):
                            print(f"{a}{b}{c}{d}")
    if q==5:
        for a in range(1,10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        for e in range(10):
                            if (a ** 5 + b ** 5 + c ** 5 + d ** 5 +e**5 == a * 10000 + b * 1000 + c * 100 + d*10+e):
                                print(f"{a}{b}{c}{d}{e}")
    if q==6:
        for a in range(1,10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        for e in range(10):
                            for f in range(10):
                                if (a ** 6+ b ** 6 + c ** 6 + d ** 6 + e ** 6+f**6 == a * 100000 + b * 10000+ c * 1000+ d * 100 + e*10+f):
                                    print(f"{a}{b}{c}{d}{e}{f}")
    if q==7:
        for a in range(1,10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        for e in range(10):
                            for f in range(10):
                                for g in range(10):
                                    if (a ** 7 + b ** 7 + c ** 7 + d ** 7 + e ** 7+ f ** 7+g**7 == a * 1000000 + b * 100000 + c * 10000 + d * 1000 + e * 100 + f*10+g):
                                        print(f"{a}{b}{c}{d}{e}{f}{g}")
    if q==8:
        for a in range(1,10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        for e in range(10):
                            for f in range(10):
                                for g in range(10):
                                    for h in range(10):
                                        if (a ** 8 + b ** 8 + c ** 8 + d ** 8 + e ** 8 + f ** 8 + g ** 8+h**8 == a * 10000000+ b * 1000000+ c * 100000+ d * 10000+ e * 1000 + f * 100 + g*10+h):
                                            print(f"{a}{b}{c}{d}{e}{f}{g}{h}")

    else:
        print("输入规范错误......")



a = "y"
while (a == "y"):
    height = float(input('请输入身高：（单位 米）'))
    weight = float(input('请输入体重：（单位 千克）'))
    bmi = weight/(height**2)
    print("你的肥胖指数为：%.2f" % bmi)
    if (bmi<18):
        print("瘦")
    if 24 >= bmi >= 18:
        print("标准")
    if (bmi <= 28) and (bmi > 24):
        print("微胖")
    if bmi >28:
        print("肥胖")
    print()
    a = input("再来一次？(y/n)")
print("""程序结束。
祝您身体健康。""")
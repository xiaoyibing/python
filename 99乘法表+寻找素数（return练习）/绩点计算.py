
w = 1
while(w == 1):
    a = float(input("请选择您要测的项目：   1.肥胖指数  2.绩点   3.离开"))
    if a == 1:
        while(1):
            print("开始测量肥胖指数。")
            # 数据输入
            height = float(input('请输入身高：（单位 米）'))
            weight = float(input('请输入体重：（单位 千克）'))
            bmi = weight / (height ** 2) # 计算肥胖指数
            print("你的肥胖指数为：%.2f" % bmi) # 输出
            # 判断肥胖
            if bmi < 18:
                print("瘦")
            if 24 >= bmi >= 18:
                print("标准")
            if bmi <= 28 and (bmi > 24):
                print("微胖")
            if bmi > 28:
                print("肥胖")
            n = input("再来一次？（y/n）")
            if n == "y":
                continue
            else:
                break
    if a == 2:
        while (1):
            print("开始计算大一上学期绩点。")
            # 成绩输入
            math = float(input("请输入您的高数B（上）成绩："))
            e1 = float(input("请输入您的大学英语（上）成绩："))
            e2 = float(input("请输入您的大学英语听说（上）成绩："))
            zhuan = float(input("请输入您的计算机学科概论成绩："))
            zheng = float(input("请输入您的思想道德修养与法制基础成绩："))
            jun = float(input("请输入您的军事理论成绩："))
            tiyv = float(input("请输入您的体育（1）"))
            xing = float(input("请输入您的形势与政策1成绩："))
            # 成绩计算：
            avg = (4/19.5)*math+(5/19.5)*e1+(2/19.5)*e2+(2/19.5)*zhuan+(3/19.5)*zheng+(2/19.5)*jun+(1/19.5)*tiyv+(0.5/19.5)*xing
            print("您的绩点为：%.2f" % avg)
            if avg >= 90:
                print("优秀。")
            if avg <90 and(avg>=60):
                print("良好。")
            if avg< 60:
                print("不及格。")
            i = input("再来一次？（y/n）")
            if i == "y":
                a = 2
            else:
                break
    if a == 3:
        break
print("程序结束。")




name=input("欢迎来到游戏，请输入您的姓名：")
i=input("请输入您的性别：")
if i=="女":
    age1=int(input("女神，请输入您的年龄："))
    if age1<20:
        print("少女英雄，")
    else:
        print("老江湖，")
else:
    age2=int(input("勇士，请输入您的年龄："))
    if age2<20:
        print("少年英雄，")
    else:
        print("老江湖，")
print("欢迎进入游戏！")


print("你来到了岔路口，")
pin=int(input("请选择您要走的方向：  1.向左  2.向右"))
if pin==1:
    print("你来到了公主的城堡。")
    pin=3
else:
    print("你来到了恶魔的森林。")
    print("你杀死了恶魔，并成功迎娶了公主。")
if pin==3:
    lan=int(input("你再次来到了岔路口，请选择：  1.向左   2.向右"))
    if lan==1:
        print("你来到了恶魔的城堡，并被恶魔杀死了。")
    else:
            print("你找到了隐藏宝箱，成功成为世界首富。")  
print("游戏结束。")
    

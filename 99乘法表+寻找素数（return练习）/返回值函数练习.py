# 返回值函数练习

import math
def hem(sex):
    if q == "1":
        q1 = int(input("你有喜欢的女明星吗？    1.有   2.没有"))
    else:
        q1 = int(input("你有喜欢的男明星吗？   1.有   2.没有"))
    if q == "1":
        q2 = int(input("看到漂亮的女生你会心动吗？   1.会   2.不会"))
    else:
        q2 = int(input("看到漂亮的男生你会心动吗？   1.会   2.不会"))
    if q == "1":
        q3 = int(input("如果有女生主动加你微信，你会同意吗   1.会   2.不会"))
    else:
        q3 = int(input("如果有男生主动加你微信，你会同意吗   1.会   2.不会"))
    if q == "1":
        q4 = int(input("你在打游戏时会主动带妹子吗？   1.会   2.不会"))
    else:
        q4 = int(input("你在打游戏时会主动带异性吗？   1.会   2.不会"))
    if q == "1":
        q5 = int(input("你有和女生畅谈过吗？    1.有   2.没有"))
    else:
        q5 = int(input("你有和男生畅谈过吗？    1.有   2.没有"))
    df = (2-q1)*20+(2-q2)*20+(2-q3)*20+(2-q4)*20+(2-q5)*20
    return df
    # 关键点，return将df带出函数外


name = input("你的名字是：")
print(f"{name}，欢迎参加脱单测试。")
q = int(input("你的性别是？   1.男   2.女"))
score = hem(q)
# 将def中带出的df值给予score
print(f"你的得分为{score}")
#从键盘上输入一个成绩，显示出其等级。
#（规则：60分以下显示不及格，60--69分显示及格，70--79分显示一般,
#80--89分显示良好，90--99分显示优秀，100分显示满分）
while(1):
    cj = int(input("请输入你的成绩："))
    if cj < 60:
        print('不及格')
    if 60 <= cj < 70:
        print('及格')
    if 70 <= cj <=80:
        print('一般')
    if 80 <= cj < 90:
        print('良好')
    if 90 <= cj <100:
        print('优秀')
    if 100==cj:
        print('满分')

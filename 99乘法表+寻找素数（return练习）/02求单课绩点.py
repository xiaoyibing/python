#从键盘上输入一个成绩，显示出绩点。
#（规则：60分以下绩点为0，60分的绩点为1.0，
#70分的绩点为2.0，80分的绩点为3.0，90分的绩点为9.0，100分的绩点为5.0）
import random

while(1):
    cj = int(input("请输入你的成绩："))
    if cj < 60:
        print('你的绩点为：0')
    if cj == 60:
        print('你的绩点为：1.0')
    if 60 < cj <= 70:
        print('你的绩点为：2.0')
    if 70 < cj <= 80:
        print('你的绩点为：3.0')
    if 80 < cj <= 90:
        print('你的绩点为：%s',4.0-0.1*(90-cj))
    if 90 < cj <= 100:
        print('你的绩点为：5.0')


num1=0
num2=f

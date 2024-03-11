
#ABC代表位置，123代表3个盘子
def num(n,A,B,C):
    if n==1:
        print(f"将{A}上的{B}移动到{C}上")
    else:
        num(n-1,A,n-1,B)
        print(f"将{A}上的{n}移动到{C}上")
        num(n-1,B,n-1,C)
num(3,"A","B","C")
#计算出1+2+3+...+100的累加和。
def digui(n):
    if n == 0:
        return 0
    else:
        return n + digui(n-1)

# 例如，计算1到5的累加和
result = digui(100)
print(result)


# 注：

1. 数据驱动

2. 分“类”尽量多

3. 主函数尽量简单

4. 提前准备，思路比过程更费时间

## 一、小细节

0. 使用**`type()`函**数来判断一个对象的数据类型。

1. 对齐`\t`    ,   不换行 `end=‘’`    ，换行  `print（）`   、  `print('\n')`

```python
print(f"{j}*{i}={j*i}\t",end='')
print()#换行，中间隔一行
print('\n')
```

2. 遇到**解方程**时，可以用for循环解决
3. 将123，111放入列表中呈现 `[[1,2,3],[1,1,1]]`    (将字符串转换为整数列表)

方法1

```python
ls1=[]
ls2=[]
for i in a:
    i=int(i)
    ls1.append(i)
for i in b:
    i=int(i)
    ls2.append(i)
ls.append(ls1)
ls.append(ls2)
```

方法2（推荐）

```python
a = '11111'
b = '22222222'
# 使用列表推导式和 map() 函数将字符串转换为整数列表
ls = [list(map(int, x)) for x in (a, b)]
```

- `map()` 是一个 Python 的内置函数，它将一个函数应用于迭代器（比如列表）中的每个元素，返回一个包含结果的迭代器。它的基本语法是：`map(function, iterable)`
- `function` 是一个对每个元素都会被调用的函数。
- `iterable` 是一个或多个序列（如列表、元组等），用来提供参数给 `function`。

-  `map()` 函数将 `function` 应用于 `iterable` 中的每个元素，并返回一个迭代器，该迭代器包含了每次函数调用的结果      

4. 依次列出字符串中的字母,并查询字数

5. ```python
   n="nihaoshijie"
   a=0
   for i in n:
       print(i)
       a+=1
   print(f"共有{a}个字母")
   ```

   

## 二、返回值return

## 三、字符串格式化

##### 1. type 查看数据类型

##### 2.数据类型转换

`int(x)`整数
`float(x)`浮点数
`str(x)`字符串

```python
# 任意类型都可以转换成字符串，
# 但字符串内必须只有数字才可以转换成浮点数，  # name=float("xiao")    不可行
# 浮点数转整数会丢失小数部分
name=float(11)
print(type(name),name)
```

##### 3.单引号，双引号

```python
name="'xiao'"
name='"xiao"'
name="\"xiao"   # 转义字符\接触引号的效用
```

##### 4.字符串拼接

```python
a="xiao"
b="bing"
print(a+b)
```

##### 5.格式化

```python
"""%f 浮点数
%s 字符串
%d 整数"""
age=12.1344
print("我姓%s,名%s,今年%5.2f岁。"%(a,b,age))
# 5.2f 中5.表示宽度控制，.2表示小数精度
```

## 四、加减乘除

```python
print(11//2)# 向下整除>>>5
print(-11//2)# >>>-6

print(2**3)   #指数
print(9%2)    # 取余数

  #  比较运算
print(f"10>=11的结果是{10>=11}")
```

- map()函数
- 这里 `lambda x: x**2` 是一个匿名函数，`map()` 函数将它应用于 `numbers` 列表中的每个元素，并将结果存储在一个迭代器中。最后通过 `list()` 将迭代器转换为列表以展示结果

```python
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # 输出 [1, 4, 9, 16, 25]
```



## 五、数据库的使用

## 六、turtle库

下载

```python
pip install turtle
```

#### 1.创建窗口

```python
import turtle as t#导入turtle库
# 创建窗口
name = t.Screen()
name.title("迷宫小游戏")#设置窗口名字

name.bgcolor('black')#设置窗口颜色
name.setup(700, 500)#窗口大小（宽，高）

name.tracer(0) #关闭动画效果，允许绘图完成后一次性显示，防止窗口更新
```

```python
name.screensize(800, 600, "pink")#(推荐)
```

#### 2.画笔形状

##### （1）导入`gif`图片做画笔形状

```python
t.register_shape('狼.gif')
t1 = t.Turtle()
t1.color("white")
t1.shape('狼.gif')
```

```
在Turtle库中，register_shape() 函数的作用是将自定义的形状注册到Turtle模块中，以便后续在画布上使用这些形状。

通常，Turtle模块提供了一些默认的形状，比如箭头、圆形等，但有时候我们需要使用自己设计的形状。register_shape() 函数就是为了解决这个问题。

它的工作原理是将用户定义的形状信息上传到Turtle模块中，并给这个形状取一个名字，以便在之后的绘图中引用。上传的形状信息通常是一个列表，其中包含一系列的坐标点，这些点连接起来就形成了所需的形状。在上传后，我们就可以通过指定这个名字来使用这个自定义的形状，比如在创建Turtle对象时设置其形状为我们自定义的形状。
```



#####  （2）现场画图形作为画笔

```python
t.begin_poly()   #开始构建画笔形状
t.fd(lenght)
t.end_poly()     #结束构建画笔形状
t.register_shape(name,t.get_poly())#注册画笔名字和形状
pen=t.Pen()
pen.shape(name)#应用
```

#####   （3）系统自带的形状

```python
t.Pen(shape='circle')# 方法一
t.shape('circle')#方法二
```

1. **箭头形状（默认形状）**：
   - 名称: "arrow" 或 "turtle"。这是Turtle初始化时的默认形状。
2. **经典形状**：
   - 名称: "classic"。类似于一个三角形，稍微不同于默认的箭头形状。
3. **圆形**：
   - 名称: "circle"。这是一个简单的圆形。
4. **方形**：
   - 名称: "square"。正方形形状。
5. **三角形**：
   - 名称: "triangle"。一个朝上的等边三角形形状

#### 3.写入字

```python
turtle.write(text, font=("font_name", font_size, "font_style"), align="alignment")
```

- `text` 参数是要绘制的文本字符串。

- `font`参数允许你指定字体的名称、大小和样式（可选）。

- `font_name` 是字体名称（例如："Arial", "Times New Roman"等）。
- `font_size` 是字体大小。
- `font_style` 是字体样式（例如："normal", "bold", "italic"等），可选参数。
- `align` 参数指定文本的对齐方式，可以是："left", "center", "right"

#### 4.其他基本语句

t.seth（0）

1. **移动海龟**：
   - 前进（向前移动）：`forward(distance)` 或 `fd(distance)`
   - 后退（向后移动）：`backward(distance)` 或 `bk(distance)` 或 `back(distance)`
   - 移动到指定坐标：`goto(x, y)` 或 `setx(x)`、`sety(y)`
2. **控制海龟的转向**：
   - 左转：`left(angle)` 或 `lt(angle)`
   - 右转：`right(angle)` 或 `rt(angle)`
3. **画笔控制**：
   - 提起画笔：`penup()` 或 `pu()`
   - 放下画笔：`pendown()` 或 `pd()`
   - 设置画笔颜色：`pencolor(color)`，例如：`"red"`, `"blue"`, `"#FF0000"`
   - 设置填充颜色：`fillcolor(color)`
4. **控制海龟的外观**：
   - 设置海龟大小：`turtlesize(stretch_wid, stretch_len, outline=None)`
   - 设置海龟形状：`shape('turtle')` 或 `shape('square')` 等
5. **控制绘图窗口**：
   - 设置窗口标题：`title("Title")`
   - 控制绘图窗口的尺寸：`setup(width, height)`
   - 清空绘图窗口：`clear()` 或 `clearscreen()`
6. **控制海龟的速度**：
   - 设置海龟速度：`speed(1)` 到 `speed(10)`，0 表示最快

7. **控制画笔的粗细**：

- 设置画笔粗细：`width(size)` 或 `pensize(size)`

8. **填充形状**：

- 开始填充：`begin_fill()`
- 结束填充：`end_fill()`

11. **颜色控制**：

- 获取当前颜色：`pencolor()` 或 `fillcolor()`
- 获取颜色列表：`colors()`

###### `RGB`颜色体系

**要输入小数（0-1之间），或者用16进制数表示颜色，如`t.pencolor("#FFFF00")`**黄色

在计算机`RGB`色彩体系中，很多颜色都有固定的英文名字，这些英文名字可以作为`colorstring`输入到t`urtle.pencolor()`函数中，也可以采用（r,g,b）形式直接输入颜色值。下面介绍几种典型的`RGB`颜色

- `RGB`小数值   `turtle.pencolor(0.63,0.13,0.94)` #三个小数值

- `RGB`数值元组      `turtle.pencolor((0.63,0.13,0.94))`  # 一个三元素元组

- 颜色字符串  `turtle.pencolor('purple')`  # 小写



12. **坐标控制**：

- 获取海龟当前位置：`position()` 或 `pos()`
- 获取海龟当前朝向角度：`heading()`

13. **绘制特殊形状**：

- 画圆：`circle(radius)`，指定半径来绘制圆
- 画正多边形：`polygon(sides, length)`，指定边数和边长来绘制多边形

14. **Turtle状态控制方法**：

- `t.clear()`从中删除所有海龟的全部绘图。将已清空的 TurtleScreen 重置为初始状态: 白色背景，无背景片，无事件绑定并启用追踪。

- `speed(speed)`：设置所有海龟的运动速度。
- `delay(delay)`：设置所有海龟的动画延迟。

15. **全局操作控制方法**：

- `done()`：使得绘图窗口保持打开状态，直到关闭。
- `reset()`：清空绘图窗口，并重置所有海龟的状态。

16. **其他控制方法**：

- `bye()`：关闭绘图窗口并退出Turtle绘图环境。
- `t.mainlop()`和`t.done()`开始事件循环 - 调用 `Tkinter` 的 `mainloop` 函数。必须作为一个海龟绘图程序的结束语句。(防止窗口关闭)

#### 5.t.mainloop()

不立即关闭

#### 6.

画笔的属性：
turtle.pensize() #设置画笔的宽度
turtle.pencolor(color) #没有参数传入，返回当前画笔颜色，color参数有三种形式传入参数，可以是字符串形式（颜色的英文，字母用小写），如"green", “red”；也可以是RGB小数值或元组值（3元组）（每个小数或元组值对应的有颜色表，感兴趣可以自己了解一下，因为鄙人也不是特别清楚颜色这块）
turtle.speed(speed) #设置画笔移动速度，画笔绘制的速度范围[0,10]整数，数字越大越快

画笔运动命令：
turtle.forward(distance) #向当前画笔方向移动distance像素长度
turtle.backward(distance) #向当前画笔相反方向移动distance像素长度
turtle.right(degree) #顺时针移动degree°
turtle.left(degree) #逆时针移动degree°
turtle.pendown() #移动时绘制图形，缺省时也为绘制
turtle.goto(x,y) #将画笔移动到坐标为x,y的位置
turtle.penup() #提起笔移动，不绘制图形，用于另起一个地方绘制
turtle.circle(radius,extent) #根据半径radius绘制extent角度的弧形，若无extent参数则画圆，radius为正(负)，表示圆心在画笔的左边(右边)画圆，参数为正则是顺时针画圆，参数为负则是逆时针画圆
turtle.setx( ) #将当前x轴移动到指定位置,y轴不变
turtlr.sety( ) #将当前y轴移动到指定位置，x轴不变
turtle.setheading(angle) #设置当前箭头朝向为angle角度,0-向右，90-向上，180-向左，270-向下
turtle.home() #设置当前画笔位置为原点，朝向东。
turtle.dot® #绘制一个指定直径和颜色的圆点
turtle.setpos(x,y)#机器小乌龟定位到x=,y=
turtle.pos() #获得当前位置
turtle.xcor() #获得X坐标
turtle.ycor() #获得Y坐标

画笔控制命令：
turtle.fillcolor(colorstring) #绘制图形的填充颜色
turtle.color(color1, color2) #同时设置pencolor=color1, fillcolor=color2
turtle.filling() #返回当前是否在填充状态
turtle.begin_fill() #准备开始填充图形
turtle.end_fill() #填充完成
turtle.hideturtle() #隐藏画笔的turtle形状
turtle.showturtle() #显示画笔的turtle形状

全局控制命令：
turtle.clear() #清空turtle窗口，但是turtle的位置和状态不会改变
turtle.reset() #清空窗口，重置turtle状态为起始状态
turtle.undo() #撤销上一个turtle动作
turtle.isvisible() #返回当前turtle是否可见
stamp() #复制当前图形
turtle.write(s [,font=(“font-name”,font_size,“font_type”)])

##### 列

###### 1.画直方图

- 描线法（推荐）（用for循环+数据库连续画线）

- 填充法（画出框架然后填充颜色）

###### 2.五角星

```python
def star(length, angle):
    t.color('yellow', 'yellow')
    t.pendown()
    t.left(angle)#星星的朝向
    t.begin_fill()
    for i in range(5):#循环5次
        t.forward(length)
        t.left(72)
        t.forward(length)
        t.right(144)
    t.end_fill()
    t.right(angle)#规正朝向
    t.penup()
```

## 七、递归

##### 列

###### 1.递归法解汉诺塔

```python
#ABC代表位置，123代表3个盘子
def num(n,A,B,C):
    if n==1:
        print(f"将{A}上的{B}移动到{C}上")
    else:
        num(n-1,A,n-1,B)
        print(f"将{A}上的{n}移动到{C}上")
        num(n-1,B,n-1,C)
num(3,"A","B","C")#可以通过改变数字，改变汉诺塔的层数
```

- 转化为turtle**图像版**的方法：
- 创建三个列表，每个列表表示一个位置，
- 通过增减列表中的数据模仿盘子的移动，
- 每次移动后都要重新画一遍三个位置上的盘子

## 八、键盘监听+鼠标监听

先设子函数，运用listen（）实现键盘监听，将键盘按键与子函数链接

```python
def move_up():
    ball.sety(ball.ycor()+5)#x轴不变，y轴加5
def move_down():
    ball.sety(ball.ycor()-5)
def move_left():
    ball.setx(ball.xcor()-5)#y轴不变，x轴减5
def move_right():
    ball.setx(ball.xcor()+5)#y轴不变，x轴加5
```

```python
name.listen()   # 键盘监听
name.onkeypress(move_up,'Up') #将ball.sety(ball.ycor()+5) 付于‘Up’键
name.onkeypress(move_down,'Down')
name.onkeypress(move_left,'Left')
name.onkeypress(move_right,'Right')
```

当按下‘Up’键时，使用函数move_up（）

##### xcor() ycor()

画笔向斜上方运动

```python
while(1):
    ball.goto(ball.xcor()+1,ball.ycor()+1)
```

`pen.xcor()`       返回海龟的 x 坐标

`pen.ycor()`       返回海龟的 y 坐标

## 九、穷举法

‘’‘’一位自幂数：独身数。三位自幂数：水仙花数。四位自幂数：四叶玫瑰数。五位自幂数：五角星数

六位自幂数：六合数。七位自幂数：北斗七星数。八位自幂数：八仙数。九位自幂数：九九重阳数
十位自幂数：十全十美数‘’‘’

```python
for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            if (a ** 3 + b ** 3 + c ** 3 == a * 100 + b * 10 + c):
                 print(f"{a}{b}{c}")
```

## 十、字典

### 创建字典

```python
a={}
```

### 增添

```python
a[11]=[aa]
a[22]=[[dd],[aa]]
```

for 循环法添加数据

```python
ls=[['9787560855295','高数第3版课本',36.00],\
    ['6921168520015','1.5L农夫山泉矿泉水',3.00],\
    ['6922868283446','99.9%杀菌湿巾',4.00],\
    ['6973870130341','1L乳酸菌饮料',4.00],\
    ['6953787302420','一支笔笔芯 20支/盒',10.00]]
```

```python
a={}
for i in range(len(ls)):
    a[ls[i][0]]=[ls[i][1],ls[i][2]]
print(a)
```

< 运行结果

```python
{'9787560855295': ['高数第3版课本', 36.0], '6921168520015': ['1.5L农夫山泉矿泉水', 3.0], '6922868283446': ['99.9%杀菌湿巾', 4.0], '6973870130341': ['1L乳酸菌饮料', 4.0], '6953787302420': ['一支笔笔芯 20支/盒', 10.0]}
```

### 修改

与增添类似，若key值相同，则新的value会覆盖旧值

```python
d = {'a': 180, "b": 175, "c": 170}
d['a'] = 185   
print(d['a'])  
>>>185    
```

### 删除

1. `del`

删除一个key

```python
d = {'a': 180, "b": 175, "c": 170}
del d['a']
print(d)
>>>{ "b": 175, "c": 170}
```

2. `clear()`

删除全部

3. pop（key）

**字典名.pop(key)
弹出指定key的键值对，key值必须给出。给定的key值不在字典中时，会报错。**

4. `popitem()`

**字典名.popitem()
说明：随机删除其中一个键值对，并返回一个键值对组成的元组**

```python
d = {'a': 180, "b": 175, "c": 170,"d": 180}
v = d.popitem()  #相当于栈出，不过每次出的是一个键值对
print(v)
print(d)
>>>('a',180)
>>>{ "b": 175, "c": 170,"d": 180}
```

### 遍历

（一）keys()

```python
for key in d.key:
    print(key)
```

（二）values()

```python
for value in d.values:
    print(value)
```

（三） key-value()

```python
for key,value in d.items():
    print(key,value)
```

### 导出字典中的数据

1. 字典名+【key】

+ []'9787560855295']一定带    ‘   ’  号

```python
a['9787560855295'] ----- ['高数第3版课本', 36.0]
a['9787560855295'][0]-----高数第3版课本
a['9787560855295'][1]------36.0
```

2. **字典名**+get(key)

```python
d = {'a': 180, "b": 175, "c": 170}      # 创建字典
print(d.get('a'))
>>>180
# 字典里面没有f，key不存在
print(d.get('f'))
>>>None
```

+ 与直接d[key]不同，当key不存在时，`**字典名**+get(key)`并不会显示错误，而是输出None

### 常见操作

- `len(dict)`输出key的个数

- `dict.keys()`输出所有的key值

- `dict.value()`输出所有value值

- `dict.items()`将字典中的key，value保存到列表中

```python
d = {'a': 180, "b": 175, "c": 170}      
dict.items()
[('a',180),('b',175),('c',170)]
```

### 字典 根据value值排序， 获取top N个元素

```python
a={'a':1,'b':5,'c':9}

ls=list(a.items())#变为列表

ls.sort(key=lambda x:x[1],reverse=True)#对列表排序

print(ls[:2])#输出前两个元素
```

## 十一、正则

就是通过一行字符串，来描述一定的规则，

正则表达式的英文为 Regular Expression，所以我们通常采用这两个单词的首几个字母合在一起，把正则表达式相关的变量名定义为 `regexp`（单数） 或 `regexps`（复数） 。

python中re模块提供了正则表达式的功能，常用的有四个方法(`match`、`search`、`findall`)都可以用于匹配字符串

[Python 正则表达式详解（建议收藏！）-CSDN博客](https://blog.csdn.net/qq_44159028/article/details/120575621?ops_request_misc=%7B%22request%5Fid%22%3A%22169927944916800226530612%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=169927944916800226530612&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-120575621-null-null.142^v96^pc_search_result_base8&utm_term=Python正则&spm=1018.2226.3001.4187)

```python
import re
```

### findall

+ `findall`是寻找所有能匹配到的字符，并以列表的方式返回
+ `.* `    表示从`txt`到`kkk`

```python
import re
a = 'dfsdhdf txt afsgdsf kkk affg'
print(re.findall(r'txt.*kkk',a))  
>>>['txt afsgdsf kkk']  #输出结果为 列表
```

#### re.S

+ `re.S`会将字符串作为一个整体，在整体中进行匹配，支持a换行

```python
import re
aa = '''dfsdhdf txt afsgds        #a换行
f kkk affg'''
print(re.findall(r'txt.*kkk',aa)) #不支持a换行
>>>[]
print(re.findall(r'txt.*kkk',aa,re.S)) 
>>>['txt afsgds\nf kkk']
```

#### 查找汉字

`[\u4E00-\u9FFF]`   

```python
text='12345一二三四五abcde一二三四五12345'
m=re.findall('[\u4E00-\u9FFF]',text)#findall可以查找匹配项,在这里会返回一个列表,也就是m
print(m)
>>>['一', '二', '三', '四', '五', '一', '二', '三', '四', '五']
```

```python
text='12345一二三四五abcde一二三四五12345'
m=re.findall('[\u4E00-\u9FFF]+',text)  #+将相邻的汉字组合成一个元素
print(m)
>>>['一二三四五', '一二三四五']
```

#### split

对字符串进行分割，并返回一个列表

```python
import re
aa = "df-sdhdf,tx-t:afsg:dsfkk;kaffg"
print(re.split(r",",aa))           #以,号进行分割
print(re.split(r",|:|-|;",aa))     #以,或者：或者-或者;进行分割
print(re.split(r",|:|-|%",aa))    #找不到的分隔符就忽略
```

```python
>>>['df-sdhdf', 'tx-t:afsg:dsfkk;kaffg']
>>>['df', 'sdhdf', 'tx', 't', 'afsg', 'dsfkk', 'kaffg']
>>>['df', 'sdhdf', 'tx', 't', 'afsg', 'dsfkk;kaffg']
```

### search and match

区别：match只能从头开始寻找

+ re.match(pattern,string)
+ group()  #返回

```python
import re
a = re.match(r'daa','daaasddaaff')  
print(a)                             #返回一个匹配对象
print(a.group())                     #返回test，获取不到则报错
b=a.group()
print(b)
print(a.span())           #返回匹配结果的位置，左闭右开区间
print(re.match('test','atestasdtest'))  #返回None
```

```python
<re.Match object; span=(0, 3), match='daa'>
daa
daa
(0, 3)
None
```

#### 功能表

| 字符 | 功能                            |
| ---- | ------------------------------- |
| .    | 匹配任意1个字符（\n除外）       |
| []   | 匹配【】中的字符                |
| \d   | 匹配数字（0-9）                 |
| \D   | 匹配非数字                      |
| \s   | 匹配空格                        |
| \S   | 匹配非空格                      |
| \w   | 匹配单词字符（0-9）（a-z）(A-Z) |
| \W   | 匹配非单词字符                  |

###### ...的用法

```python
import re
a = re.starch('...','testasdtest')  #几个.表示几个字符（从头开始）
print(a.group())                        
>>>tes
```

```python
c = re.match('te..','testasdtest')  
print(b.group()) 
>>>test
```

```python
b = re.match('ab.','testasdtest')  
print(b) 
>>>None

```

注意：

```python
b = re.match('ab.','testasdtest')  
print(b.group())  #错误代码 
>>>'NoneType' object has no attribute 'group'
```

```python
import re
print(re.match('12[234]','232s12testasdtest'))
>>>None
print(re.search('12[135]','231252s12testasdtest').group()) 
>>>125
```

### 提取两个字符串之间的内容

```python
import re
 
s = "AwdnmdB"
a = r'A(.*?)B'
result = re.findall(a,s)
print(result)
 
//打印结果为：wdnmd
```

## 十二、ASCII数值转换

###### `chr(int)`

范围在range(0,256)（即0-255）内,返回对应的字符。

###### `ord()`

返回对应的ASCII数值

```python
ord('a')
>>>97
chr(97)
>>>'a'
```

###### 输出【A-Z】：

+ ```python
  for i in range(26):
      print(chr(ord('A')+i))
  ```

###### 用于判断字符是否是汉字：

x0400-x052f (俄语) xAC00-xD7A3 (韩文)**u0800-u4e00** (日文)

+ ```python
  def chinese(n):  # 第n个字符是汉字的字符串
      return 19968 <= ord(n) <= 40959
  print(chinese('1'))  
  >>>False
  print(chinese('你')) 
  >>>True
  #缺点：只能判断一个字符
  ```

  判断并输出：

  ```python
  def chinese(n):  # 第n个字符是汉字的字符串
      return 19968 <= ord(n) <= 40959
  a='aff水电费f123  大幅www  244增加'
  for i in a:
      if chinese(i)==True:
          print(i,end='')  
  >>>'水电费大幅增加'
  ```

  ```python
  import re
  str = '输入需要匹配的字符'
  
  jap = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\uAC00-\uD7A3]')  # \uAC00-\uD7A3为匹配韩文的，其余为日文
  if jap.search(str):
      print('Yes')
  ```

  

# 十三、随机random库

1. #### `random.random()`: 返回随机生成的一个浮点数，范围在[0,1)之间

```python
import random
print(random.random())
```

2. #### `random.uniform(a, b)`**:返回随机生成的一个浮点数，范围在[a, b)之间**

```python
import random
print(random.uniform(1,5))
```

3. #### `random.randint(a,b)`

   + 参数1、参数2必须是整数
   + 函数返回参数1和参数2之间的任意整数， 闭区间

```python
import random
result = random.randint(1,10)      #返回 [1, 10] 之间的任意整数
print("result: ",result)
```

```python
result:6
```

# 十四、time库

`import time`

`time.sleep(10)`

休息10秒

# 十五，ascii码

将字符转为 ASCII 码，可以使用 `ord()` 函数。它返回给定字符的 ASCII 码值：

```c
char = 'a'
ascii_val = ord(char)
print(ascii_val)

```

将 ASCII 码值转为字符，可以使用 `chr()` 函数。它返回给定 ASCII 码值对应的字符：

```c
ascii_val = 97
char = chr(ascii_val)
print(char)

```

### 判断input的数据类型

str.isdigit()为True表示输入的所有字符都是数字
str.isalnum()为True表示输入的所有字符都是数字或者字母
str.isalpha()为True表示输入的所有字符都是字母
str.isdigit()为True表示输入的所有字符都是数字
str.islower()为True表示输入的所有字符都是小写
str.isupper()为True表示输入的所有字符都是大写
str.istitle()为True表示输入的所有单词都是首字母大写，像标题
str.isspace()为True表示输入的所有字符都是空白字符、\t、\n、\r

更新一下：
注意，用isdigit()来判断小数，比如3.14就会返回FALSE。
isdigit()只是判断输入的是不是纯数字，不是判断你输入的是不是一个数，这个方法只是判断你输入的是什么字符，并不是判断你输入的是什么类型，因为无论如何，输入的值都为字符串类型，小数中有小数点，当然会返回FALSE了。
如何判断输入是不是小数，首先判断输入有没有小数点，几个小数点，小数点的位置、再按照小数点进行切片，切为两片，判断每一片是否都为纯数字

# 十六，abs

绝对值函数

`abs()` 是Python内置函数之一，用于返回一个数的绝对值。绝对值是一个数到零的距离，无论该数是正数还是负数，其绝对值总是非负的，`abs()` 分别计算了 `-5` 和 `3.14` 的绝对值，分别得到 `5` 和 `3.14`。这个函数在处理数值时非常实用，特别是在需要获取距离或大小的场景中。

```python
num1 = -5
num2 = 3.14

abs_num1 = abs(num1)
abs_num2 = abs(num2)

print(abs_num1)  # 输出：5
print(abs_num2)  # 输出：3.14

```

![image-20240124180306448](./../../../Code/photo/image-20240124180306448.png)

# 十七，随机数

1. 包含上下限：[a, b]

```c
random.randint(a,b)
    random.randint(1,50)#随机生成最小值为1，最大值为50的整数（可以等于上下限）
random.randint(20, 20)  #上下限一样时结果永远是20 

```

2、不包含上限：[a, b）

参数a是下限，参数b是上限，生成的随机数n: a <= n < b。

```c
random.randrange(a, b)

```

- randint和randrange的区别：
  randint 产生的随机数区间是包含左右极限的，也就是说左右都是闭区间的[1, n]，能取到1和n。
  而 randrange 产生的随机数区间只包含左极限，也就是左闭右开的[1, n)，1能取到，而n取不到。
  randint 产生的随机数是在指定的某个区间内的一个值，而 randrange 产生的随机数可以设定一个步长，也就是一个间隔。
  randint 无法设定步长，会报错

3、# 随机选取指定范围内指定基数递增集合中的随机数
从指定范围内，按指定基数递增的集合中 获取一个随机数。如：random.randrange(10, 100, 2)，结果相当于从[10, 12, 14, 16, … 96, 98]序列中获取一个随机数。random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效

```c
random.randrange([start], stop[, step])

```

1、0-1之间的随机浮点数

0 <= n < 1.0

```c
random.random() #用于生成一个0到1的随机符点数: 0 <= n < 1.0

```

2、随机浮点数：

```c
random.random() #用于生成一个0到1的随机符点数: 0 <= n < 1.0

```

random.uniform(a, b)，用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a。
（random.uniform()可以允许下限大于上限，不会报错，随机结果在a和b之间，可以等于上下限）

```c
random.uniform(1, 10)  #随机生成1到10之间的浮点数，可等于1或10
random.uniform(10, 1)  #随机生成1到10之间的浮点数，可等于1或10

```

1、随机字符

```c
random.choice(sequence)

```

random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence。

```c
print(random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'))
print(random.choice("学习Python"))
print(random.choice(["JGood", "is", "a", "handsome", "boy"]))
print(random.choice(("Tuple", "List", "Dict")))
u
P
boy
Tuple

```

2、多个字符中生成指定数量的随机字符：

print random.sample(‘zyxwvutsrqponmlkjihgfedcba’,5)

从a-z A-Z 0-9生成指定数量的随机字符：

```c
 a_str = ''.join(random.sample(string.ascii_letters + string.digits, 5)) #生成5位随机字符，包括大小写字母和数字

```

```c
join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

语法：str.join(sequence)

实例：
s1 = “-”
s2 = “”
seq = (“r”, “u”, “n”, “o”, “o”, “b”) # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))
以上实例输出结果如下：
r-u-n-o-o-b
runoob
```

3、多个字符中选取指定数量的字符组成新字符串：

```c
random.sample(sequence, k)

```

四、打乱排序

```c
random.shuffle(x[, random])

```

random.shuffle(x[, random])，用于将一个列表中的元素打乱。

```c
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,"Python", "is", "powerful", "simple"]
print(items)
random.shuffle(items)
print(items)

```

```c
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'Python', 'is', 'powerful', 'simple']
['Python', 1, 'is', 3, 2, 6, 'simple', 9, 'powerful', 4, 5, 8, 0, 7]
```


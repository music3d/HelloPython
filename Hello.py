"""
print("Hello World!")

## python保留字
import keyword
keyword.kwlist

## 注释
#  第一个注释
print("Hello, Python!") # 第二个注释

#  多行注释
'''
'''

"""
"""
print("Hello, Python!")

## 行与缩进
if True:
    print("True")
else:
    print("False")

'''
## import与from...import
import sys
print("命令行参数为：")
for i in sys.argv:
    print(i)
print("\n python 路径为",sys.path)

from sys import argv,path
print("path:" ,path) #  因为已经导入path成员，所以此处引用时不需要加sys.path
'''

## isinstance和type的区别
'''
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''
class A:
    pass
class B(A):
    pass
print(isinstance(A(),A))
print(type(A())==A)
print(isinstance(B(),A))
print(type(B())==A)


## 逆向读取字符实例
input = "I like runoob"
inputWords = input.split(' ')
inputWords
inputWords = inputWords[-1::-1]
inputWords
output = ' '.join(inputWords)
output
# 函数方法
def reverseWords(input): 
      
    #  通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ") 
  
    #  翻转字符串
    #  假设列表 list = [1,2,3,4],  
    #  list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样) 
    #  inputWords[-1::-1] 有三个参数
    #  第一个参数 -1 表示最后一个元素
    #  第二个参数为空，表示移动到列表末尾
    #  第三个参数为步长，-1 表示逆向
    inputWords=inputWords[-1::-1] 
  
    #  重新组合字符串
    output = ' '.join(inputWords) 
      
    return output 
  
if __name__ == "__main__": 
    input = 'I like runoob'
    rw = reverseWords(input) 
    print(rw)


## Set集合
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
student
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
a
b
a - b #  a 和 b 的差集
a | b #  a 和 b 的并集
a & b #  a 和 b 的交集
a ^ b #  a 和 b 中不同时存在的元素


## Dictionary字典
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name':'runoob','code':1,'site':'www.runoob.com'}
dict['one']  #  输出键为 'one' 的值
dict[2] #  输出键为 2 的值
tinydict #  输出完整的字典
tinydict.keys() #  输出所有键
tinydict.values() #  输出所有值

# 构造函数 dict() 可以直接从键值对序列中构建字典如下：
dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
{x: x**2 for x in (2,4,6)}
dict(Runoob=1, Google=2, Taobao=3)
{} # 创建空字典


## Python数据类型转换
# 只需要将数据类型作为函数名即可
'''
int(x [,base]) # 将x转换为一个整数
float(x) # 将x转换到一个浮点数
complex(real [,imag]) # 创建一个复数
str(x) # 将对象 x 转换为字符串
repr(x) # 将对象 x 转换为表达式字符串
eval(str) # 用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s) # 将序列 s 转换为一个元组
list(s) # 将序列 s 转换为一个列表
set(s) # 转换为可变集合
dict(d) # 创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s) # 转换为不可变集合
chr(x) # 将一个整数转换为一个字符，与ord()互为反函数。
ord(x) # 将一个字符转换为它的整数值，ASCII码或者Unicode码
hex(x) # 将一个整数转换为一个十六进制字符串
oct(x) # 将一个整数转换为一个八进制字符串
'''


## Python身份运算符
# 身份运算符用于比较两个对象的存储单元
a = 20
b = 20
a is b
id(a) == id(b)
b = 30
a is b
a is not b

# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个， 
# == 用于判断引用变量的值是否相等。


## Python运算符优先级
# 以下列出了从最高到最低优先级的所有运算符：
'''
**                          指数 (最高优先级)
~ + -                       按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //                    乘，除，取模和取整除
+ -                         加法减法
>> <<                       右移，左移运算符
&                           位 'AND'
^ |                         位运算符
<= < > >=	                比较运算符
<> == !=	                等于运算符
= %= /= //= -= += *= **=	赋值运算符
is is not	                身份运算符
in not in	                成员运算符
and or not	                逻辑运算符
'''


## Python数字(Number)
# Python 数字数据类型用于存储数值。
# 数据类型是不允许改变的,这就意味着如果改变数字数据类型的值，将重新分配内存空间。
var1 = 1
var2 = 2
var3 = 3

# del语句删除一些数字对象的引用
del var1, var2 # 可同时删除多个对象
var1 # 将会报错
var2 # 将会报错
var3

# Python 支持三种不同的数据类型
# 整型(Int)、浮点型(float)、复数(complex)
10
-789
-0x26

0.0
15.20
-256.21
32.6e+18
-50.
30.2E-12

3.14j
45.j
9.322e-36j
3e+26J

# 可以使用十六进制和八进制代表整数
number = 0xFFFF # 十六进制
number
number = 0o7777
number


## Python数字类型转换
# 数据类型的转换，你只需要将数据类型作为函数名即可。
x = 1
y = 2
int(x) # 将x转换为一个整数。
float(x) # 将x转换到一个浮点数。
complex(x) # 将x转换到一个复数，实数部分为 x，虚数部分为 0。
complex(x,y) # 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。


## Python数字运算
# 在交互模式中，最后被输出的表达式结果被赋值给变量 _ 。
tax = 12.5 / 100
price = 100.50
price * tax
price + _
round(_, 2)
# 此处， _ 变量应被用户视为只读变量。


## 数学函数
'''
abs(x)          返回数字的绝对值，如abs(-10) 返回 10
ceil(x)         返回数字的上入整数，如math.ceil(4.1) 返回 5
exp(x)          返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)         返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)        返回数字的下舍整数，如math.floor(4.9)返回 4
log(x) 	        如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x) 	    返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...) 返回给定参数的最大值，参数可以为序列。
min(x1, x2,...) 返回给定参数的最小值，参数可以为序列。
modf(x) 	    返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	    x**y 运算后的值。
round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x) 	    返回数字x的平方根。
'''


## 随机数函数
# 随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
'''
choice(seq)     从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])   从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()        随机生成下一个实数，它在[0,1)范围内。
seed([x])       改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)    将序列的所有元素随机排序
uniform(x, y)   随机生成下一个实数，它在[x,y]范围内。
'''


## 三角函数
'''
acos(x)     返回x的反余弦弧度值。
asin(x)     返回x的反正弦弧度值。
atan(x)     返回x的反正切弧度值。
atan2(y, x) 返回给定的 X 及 Y 坐标值的反正切值。
cos(x)      返回x的弧度的余弦值。
hypot(x, y) 返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)      返回的x弧度的正弦值。
tan(x)      返回x弧度的正切值。
degrees(x)  将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)  将角度转换为弧度
'''


## 数学常量
import math
math.pi
math.e


## Python访问字符串中的值
# Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
# Python 访问子字符串，可以使用方括号来截取字符串，如下实例：
var1 = "Hello World!"
var1[0]


## Python字符串更新
# 你可以截取字符串的一部分并与其他字段拼接
var1[:6] + 'Python!' #[:6]表示从下表为6的字符开始进行替换，一直替换至结尾不管被替换字符的长短。


## Python转义字符
r'''
\(在行尾时) 续行符
\\      反斜杠符号
\'      单引号
\"      双引号
\a      响铃
\b      退格(Backspace)
\000    空
\n      换行
\v      纵向制表符
\t      横向制表符
\r      回车
\f      换页
\oyy    八进制数，yy代表的字符，例如：\o12代表换行
\xyy    十六进制数，yy代表的字符，例如：\x0a代表换行
\other  其它的字符以普通格式输出
'''


## Python列表脚本操作符
len([1, 2, 3])
[1, 2, 3] + [4, 5, 6]
['Hi!'] * 4
3 in [1, 2, 3]
for x in [1, 2, 3]:x


## Python列表截取与拼接
# 截取
L = ['Baidu', 'Alibaba' ,'Tencent']
L[2] # 读取第三个元素
L[-2] # 从右侧开始读取倒数第二个元素
L[1:] # 输出从第二个元素开始后的所有元素

# 拼接
squares = [1, 4, 9]
squares += [16, 25, 36]
squares


## 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
x[0]
x[0][1]


## Python3元组
# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
tup1 = ('Baidu', 'Alibaba', 'Tencent')
tup2 = (1, 2, 3)
tup3 = "a", "b", "c" # 不需要括号也可以
type(tup3)

# 创建空元组
tup1 = ()

# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
tup1 = (10)
type(tup1) # 不加逗号，类型为整型
tup1 = (10, )
type(tup1) # 加上逗号，类型为元组


## Python3字典
# 字典是另一种可变容器模型，且可存储任意类型对象。
d = {1:'a', 2:'b', 3:'c'}
# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
d[1]

# 修改字典
d[2] = 'e'
d[4] = 'd'
d

# 删除字典元素
del d[1] # 删除键 1
d.clear() # 清空字典
d
del d # 删除字典
d # 将会报错


## Python3集合
# 集合（set）是一个无序的不重复元素序列。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。 
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
basket # 会把set中的重复值去除

# 两个集合间的运算
a = set('abracadabra')
b = set('alacazam')
a
b
a - b # 集合a中包含而集合b中不包含的元素
a | b # 集合a或b中包含的所有元素
a & b # 集合a和b中都包含了的元素
a ^ b # 不同时包含于a和b的元素

"""#全文引号结束
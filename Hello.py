"""##全文引号开始
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
# 可以使用大括号 { } 或者 set() 函数创建集合，
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。 
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


## 集合的基本操作
# 添加元素
thisset = set(("Baidu", "Alibaba", "Tencent"))
thisset.add("Huawei")
thisset

# 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等
thisset.update({3,6})
thisset
thisset.update([0,3],[3,6])
thisset

# 移除元素
thisset.remove(3)

# 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。
thisset.discard('6')
thisset

# 我们也可以设置随机删除集合中的一个元素
x = thisset.pop()
x
# 多次执行测试结果都不一样

# 计算集合元素个数
len(thisset)

# 清空集合
thisset.clear()
thisset

# 判断元素是否在集合中存在
thisset = set(("Baidu", "Alibaba", "Tencent", "Huawei"))
"Huawei" in thisset
"360" in thisset


## Python编程第一步
# Fibonacci series 斐波那契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

# end关键字
# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
a, b = 0, 1
while b < 1000:
    print(b, end = ',')
    a, b = b, a+b


## 迭代器
# 两个基本方法：iter()和next()
list = [1,2,3,4]
it = iter(list)
next(it)
next(it)
next(it)
next(it)

# 使用for语句遍历
for x in it:
    print(x)


## 创建迭代器
# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


## StopIteration
# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，
# 在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)


## 生成器
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，
# 返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
import sys

def fibonacci(n):
    a,b,counter = 0,1,0
    while True:
        if(counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1

f = fibonacci(10)

while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()


## Python函数
# return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
# 默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。
def hello():
    print("Hello World!")

hello()

# 带上参数变量
def area(width, heigth):
    return width*heigth

def print_welcome(name):
    print("Welcome", name)

print_welcome("MJ")
w = 4
h = 5
print(area(w,h))


## 可更改(mutable)与不可更改(immutable)对象
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
# python 传不可变对象实例
def ChangeInt(a):
    a = 10
b = 2
ChangeInt(b)
print(b) # 结果是2

# 传可变对象实例
def changeme(mylist):
    '修改传入的列表'
    mylist.append([1,2,3,4])
    print("函数内取值：", mylist)
    return

# 调用changeme函数
mylist = [10,20,30,40]
changeme(mylist)
print("函数外取值：", mylist)


## 参数
# 以下是调用函数时可使用的正式参数类型
# 必须参数、关键字参数、默认参数、不定长参数

# 必须参数
# 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

# 关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
def printinfo( name, age ):
    print ("名字: ", name)
    print ("年龄: ", age)
    return

# 调用
printinfo( age=50, name="MJ" )

# 默认参数
# 调用函数时，如果没有传递参数，则会使用默认参数。
# 以下实例中如果没有传入 age 参数，则使用默认值：
def printinfo(name,age=35):
    print("名字：", name)
    print("年龄：", age)
    return

# 调用
printinfo(age=50, name="MJ")
print("-------------------")
printinfo(name="MJ")

# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数。
# 这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def printinfo(arg1, *vartuple):
    print("输出：")
    print(arg1)
    print(vartuple)

# 调用
printinfo(70,60,50)

# 还有一种就是参数带两个星号 **基本语法如下：
# 加了两个星号 ** 的参数会以字典的形式导入。
def printinfo(arg1, **vardict):
    print("输出：")
    print(arg1)
    print(vardict)

# 调用
printinfo(1,a=2,b=3)

# 声明函数时，参数中星号 * 可以单独出现，例如:
def f(a,b,*,c):
    return a+b+c
# 如果单独出现星号 * 后的参数必须用关键字传入。
f(1,2,3) # 报错
f(1,2,c=3) # 正常


## 匿名函数
# python 使用 lambda 来创建匿名函数。
# lambda只是一个表达式，函数体比def简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。 
# lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。

# 语法
# lambda 函数的语法只包含一个语句
sum = lambda arg1, arg2: arg1 + arg2

# 调用
sum(10,20)
sum(20,20)


## return语句
# return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。
# 不带参数值的return语句返回None。
def sum(arg1,arg2):
    total = arg1 + arg2
    print(total)
    return total
total = sum(10,20)
print(total)


## 变量作用域
# Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
# Python的作用域一共有4种
# L(Local)局部作用域
# E(Enclosing)闭包函数外的函数中
# G(Global)全局作用域
# B(Built-in)内置作用域(内置函数所在模块的范围)
# 以L –> E –> G –>B 的规则查找
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域

# 内置作用域是通过一个名为 builtin 的标准模块来实现的，
# 但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它。
# 在Python3.0中，可以使用以下的代码来查看到底预定义了哪些变量:
import builtins
dir(builtins)

# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
# 也就是说这些语句内定义的变量，外部也可以访问
if True:
    msg = "Who am i"
msg # 外部可以访问

def test():
    msg_inner = "Who am i"
msg_inner # 报错

# 全局变量和局部变量
total = 0 # 全局变量
def sum(arg1,arg2):
    total = arg1+arg2 # total在这里是局部变量
    print("函数内使局部变量：",total)
    return total
sum(10,20)
print("函数外是全局变量：",total)

# global和nonlocal关键字
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
num = 1
def fun1():
    global num # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)

# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
def outer():
    num = 10
    def inner():
        nonlocal num # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()


## Python数据结构
# 列表list
'''
list.append(x) 	把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L) 	通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x) 	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，
例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x) 	删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i]) 	从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。
元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，
你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear() 	移除列表中的所有项，等于del a[:]。
list.index(x) 	返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x) 	返回 x 在列表中出现的次数。
list.sort() 	对列表中的元素进行排序。
list.reverse() 	倒排列表中的元素。
list.copy() 	返回列表的浅复制，等于a[:]。 
'''

# 将列表当做堆栈使用
# 列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）。
# 用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。
stack = [1,2,3]
stack.append(4)
stack.append(5)
stack
stack.pop()
stack
stack.pop()
stack.pop()
stack

# 将列表当做队列使用
# 也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。
# 在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。 
from collections import deque
queue=deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
queue.append('Graham')
queue
queue.popleft()
queue.popleft()
queue

# 列表推导式
vec = [1,2,3]
[3*x for x in vec]

[[x,x**2] for x in vec]
[(x,x**3) for x in vec]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

# 可以用if子句作为过滤器
[3*x for x in vec if x > 1]
[3*x for x in vec if x < 2]

# 关于循环和其它技巧
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
[x*y for x in vec1 for y in vec2] # 先后面的循环在前面的循环
[x+y for x in vec1 for y in vec2]
[vec1[i]*vec2[i] for i in range(len(vec1))]

# 列表推导式可以使用复杂表达式或嵌套函数
[str(round(355/113, i)) for i in range(1, 6)]
"""##全文引号结束
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

"""#全文引号结束
## 数学函数

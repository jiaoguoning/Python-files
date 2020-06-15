#attend 的用法
L=[1,1.3,'2','china',['I','am','another','list']]
L.append([5])
print(L)
L.append('a')
print(L)

#extend方法只能在末尾添加列表，append方法既能添加一个值，也能添加一个列表
L=[1,1.3,'2','china',['I','am','another','list']]
L.append([5])
print(L)
L.append('a')
print(L)

# clear()fangfa 用于清空列表
field=['study','python','is','happy']
field.clear()
print('field调用clear方法后的结果：',field)

# copy()方法用于复制列表
field=['study','python','is','happy']
copyfield=field.copy()
copyfield2=field[:]
print('复制操作的结果：',copyfield)
print('使用列表分片实现复制的效果',copyfield2)
field.append(999)
print(field)
print(copyfield)
print(copyfield2)
L=[1,2,3,4,5]
LL=[7,8,9]
LL=L
print(L)
print(LL)
L.clear();
print(L)
print(LL)

#extend()方法用于在列表末尾一次性追加另一个序列中的多个值
#语法：list.extend(seq)
a=['hello','world']
b=['python','is','funny']
a.extend(b)
a.extend([1,2,3])
print(a)

#extend()方法和序列相加的区别
#序列相加
a=['hello','world']
b=['python','is','funny']
print(a+b)
print(a)

#用分片赋值实现和extend()相同的结果
a=['hello','world']
b=['python','is','funny']
a[len(a):]=b
print(a)

#index（）方法用于从列表中找出某个值第一个匹配项的索引位置。
#语法：list.index(obj)
field=['hello','world','python','is','funny']
print('hello的索引位置为：',field.index('hello'))
print('python的索引位置为：',field.index('python'))
#index的作用是从列表中找到某个值的索引位置
L=[1,1,2,3,4]
print('3的索引位置为：',L.index(3))

#insert的用是把元素插入到索引位置
#insert（）语法:list.insert(index,obj)
num=['a','b','c']
print('插入之前的num:',num)
num.insert(2,'hello word')
#插入位置在b之后，c之前
print('插入之后的num：',num)

#pop()方法用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
#语法:list.pop()
# pop方法是唯一一个既能修改列表又能返回元素值的列表方法

field=['hello','world','python','is','funny']
print(field.pop())
print('移除元素后的field：',field)

print(field.pop(3))
print('移除元素之后的field：',field)

print(field.pop(0))
print('移除元素之后的field：',field)

# remove（）方法用于移除列表中某个值的第一个匹配项
# remove（）方法的语法如下：
# list.remove(obj)
field=['女排','精神','中国','精神','学习','精神']
print('移除前列表field：',field)
field.remove('精神')
print('移除后列表field：',field)

# reverse()方法用于反向列表中的元素
# 语法：list.reverse()
num=[1,2,3]
print('列表反转前num：',num)
num.reverse()
print('列表反转后：',num)

num=[1,2,3]
print('使用reversed函数翻转结果：',list(reversed(num)))
print('num的结果是：',num)
# num保持了原样

# sort()方法用于对原列表进行排序，如果指定参数，就是用参数指定的比较方法进行排序
# 语法：list.sort()
num=[5,8,1,3,6]
num.sort()
print('num调用sort方法后:',num)
# num本身也变了
num=[5,8,1,3,6]
n=num.sort()
print('变量n的结果是：',n)
print('列表num排序后的结果是：',num)
# sort（）方法修改了列表num，但是返回的是空值

num=[5,8,1,3,6]
n=num
n.sort()
print('变量n的结果是：',n)
print('num的结果是：',num)
# n和num指向的事同一个列表
n=num[:]
n.sort()
print('变量n的结果是：',n)
print('num的结果是：',num)
# 分片保留了副本，num没有变，n被排序了

num=[5,8,1,3,6]
n=sorted(num)
print('变量n的操作结果是：',n)
print('num的结果是：',num)
# num保持了原样
print(sorted('python'))

# 高级排序
field=['study','python','is','happy']
field.sort(key=len)
print(field)
field.sort(key=len,reverse=True)
print(field)
num=[5,8,1,3,6]
num.sort(reverse=True)
print(num)

#count()方法用于统计某个元素在列表中出现的次数
#语法：list.count(obj)
field=['h','e','l','l','o','w','o','r','l','d']
print(field)
#统计列表中的字符个数
print('列表field中，字母o的个数：',field.count('o'))
print('列表field中，字母l的个数：',field.count('l'))
print('列表field中，字母a的个数：',field.count('a'))
listobj=[123,'hello','world',123]
listobj=[26,'hello','world',26]
print('数字26的个数：',listobj.count(26))
print('hello的个数：',listobj.count('hello'))
print(['a','c','a','f','a'].count('a'))
mix=[[1,3],5,6,[1,3],2]
print('嵌套列表mix中列表[1,3]的个数为：',mix.count([1,3]))

L=[1,1.3,'2','china',['I','am','another','list']]
print(L[-1:-4:-1])
print(len(L))
#当序列中的数据类型都是整数或者浮点数的时候才能求最大值和最小值
nums=[0.1,1.3,2,50]
print(nums)
print(min(nums))
print(max(nums))
greeting=list("hi")
print(greeting)
#列表分片赋值:可以使用与原序列不等长的序列将分片替换
greeting[1:]=list("ello")
print(greeting)

#分片赋值
field=list('ae')
print(field)
#可以在不替换任何原有元素的情况下在任意位置插入新元素
#这个例子是替换了一个空分片，实际是插入一个序列
#分片赋值比append（）方法功能要强大，因为append只能在末尾进行添加
field[1:1]=list('bcd')
print(field)
boil=list('女排夺冠了')
print(boil)
boil[2:2]=list('2016年奥运会')
print(boil)

#分片赋值实现删除功能
field=list('abcde')
print(field)
field[1:4]=[]
print(field)
boil=list('女排2016年奥运会夺冠了')
print(boil)
boil[2:10]=[]
print(boil)

#亲爱的你好，你本月的花费是，话费余额为
print("亲爱的%s你好，您本月的花费为%d,本月余额为%f" % ('焦国宁',10,1.28))
#%后面如果只有一个字符串或是其他的，只有一个，可以不用括号括起来
print("亲爱的%s你好，您本月的话费余额为%d,剩余的费用为%f"%('jiaoguoning',99,98.6))





#the first homework
import random
s=random.randint(0,9)
#随机数大小区别左或右
if s>=5:
    s="左"
else:
    s="右"
a=random.randint(1,9)
b=random.randint(1,6)
print("请%s侧第%d排第%d列的同学回答老师问题！"%(s,a,b) )

#the second homework
s=list(input('输入英文字符串：'))
a=s.copy()
a.reverse()
if s==a:
    print('是回文字符串')
else:
    print('不是回文字符串')

#the thrid homework
num0=list(input('输入2018年的某一天：'))
x=num0.index('/')
if x>1:
    a=int(num0[1])
    num1=10+a
else:
    b=int(num0[0])
    num1=b
s=int(x)
y=num0[s+1:]
ss=len(y)
if ss>1:
    n=int(y[0])
    m=int(y[1])
    num2=n*10+m
else:
    n=int(y[0])
    num2=n

if num1==1:
    L=num2
    print('这是2018年的第%d天'%L)
elif num1==2:
    L=31+num2
    print('这是2018年的第%d天'%L)
elif num1==3:
    L=31+28+num2
    print('这是2018年的第%d天'%L)
elif num1 == 4:
    L = 31 +28+31+ num2
    print('这是2018年的第%d天' % L)
elif num1 == 5:
    L = 31 +28+31+30+ num2
    print('这是2018年的第%d天' % L)
elif num1 == 6:
    L = 31 +28+31+30+31+ num2
    print('这是2018年的第%d天' % L)
elif num1 == 7:
    L = 31 +28+31+30+31+30+ num2
    print('这是2018年的第%d天' % L)
elif num1 == 8:
    L = 31 +28+31+30+31+30+31+ num2
    print('这是2018年的第%d天' % L)
elif num1 == 9:
    L = 31 +28+31+30+31+30+31+31+ num2
    print('这是2018年的第%d天' % L)
elif num1 == 10:
    L = 31 +28+31+30+31+30+31+31+30+ num2
    print('这是2018年的第%d天' % L)
elif num1 == 11:
    L = 31 +28+31+30+31+30+31+31+30+31+ num2
    print('这是2018年的第%d天' % L)
elif num1==12:
    L = 31 +28+31+30+31+30+31+31+30+31+30+ num2
    print('这是2018年的第%d天' % L)

# 在远程端对work1的内容进行删改和提交

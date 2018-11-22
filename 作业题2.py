#The homework of No.1
for a in range(1,3000):
    if (a%1==0 and a%3==0and a%7==0and a%9==0and a%2==1 and a%4==1 and a%6==3and a%8==1 and a%5==4):
         print('输出最小值为：%d'%a)

#The homework of No.2
a=666
n=int(input('请输入想转化成的第几进制：'))
L=[]
while a>=1:
    s=int(a%n)
    L.append(s)
    a = (a - s) / n
    continue
L.pop(-1)
L.reverse()
for i in L :
    print(i ,end="")

#The homework of No.3
a=int(input('Please input a number:'))
b=int(input('Please input a number:'))
c=int(input('Please input a number:'))
d=int(input('Please input a number:'))
e=int(input('Please input a number:'))
f=int(input('Please input a number:'))
g=int(input('Please input a number:'))
h=int(input('Please input a number:'))
l=int(input('Please input a number:'))
p=int(input('Please input a number:'))
L=[a,b,c,d,e,f,g,h,l,p]
s=L.copy()
x=max(s)
q=int(L.index(x))
s.pop(q)
print(max(s))

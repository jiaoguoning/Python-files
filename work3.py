#九九乘法表
for x in range(1,10):
    for y in range(1,x+1):
            print('%s*%s=%s  '%(x,y,x*y),end="  ")
    print()


#从一加到一百
print(sum(range(1,101)))

#能被4和400整除，但不能被100整除
a=int(input("Enter"))
if a%4==0 and a%100!=0 or a%400==0:
    print("%d是闰年"%a)
else:
    print("%d不是闰年"%a)

s="Just do IT"
print(s.find("do"))
print(s.find("sa"))

#join的用法   例如sq中的字符串以+相连接
sq=['1','1.3','china']
s="+"
print(sq)
print(s.join(sq))

#upper and lower 是让字符串中的英文字母改变大小写
s="Just do IT"
t=s.lower()
print(s)
print(t)

#让后面的新的字符替换下旧的
s="Just do IT"
t=s.replace("IT","it")
print(s)
print(t)

#返回到列表中去的是字符串按split 中的分隔开的一个个的单个元素
s="Just do IT"
t=s.split(" ")
print(s)
print(t)
#返回的值是列表而不是其他的字符串

#删除开头的字符
s="Just do IT"
t=s.strip("Ju")
print(s)
print(t)

#把大写字母改写为小写把小写改为大写
s="Just do IT"
t=s.swapcase()
print(s)
print(t)



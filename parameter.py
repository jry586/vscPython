#parameter.py

def parameter(s):
    s[0],s[1]=s[1],s[0]
    
s=eval(input("请输入一个两个元素的列表："))
parameter(s)
print("你输入的元素是{}".format(s))

    
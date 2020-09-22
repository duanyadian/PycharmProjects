"""
#定义并声明函数
def sum(sum1,sum2):
    "两数之和"
    return sum1+sum2

# 调用函数
print (sum(5,6))

"""
"""
def num (num1,num2):
    "两数之和"
    if not (isinstance(num1,(int,float)) and isinstance(num2,(int,float))):
            raise TypeError("参数类型错误！")
    return num1+num2

print (num("er",6))
"""
def division(num1,num2):
    #求商和余数
    a = num1%num2
    b = (num1-a) /num2
    return a,b

num1,num2=division(9,4)
tuple=division(9,4)

print(num1,num2)
print(tuple)
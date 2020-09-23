count=1
sum=0
# while count<=100:
#     sum=sum+count
#     count=count+1
# print(sum,count)

# while count<=100:
#     sum=sum+count
#     if (sum > 1000):
#         break
#     count=count+1
# print(sum,count)

# while count<=100:
#     sum=sum+count
#     if (sum % 2 ==0):
#         continue
#     count=count+1
# print(sum,count)

while count<=100:
    if (count % 2 == 0): # 双数时跳过输出
        count=count+1
        continue
    sum=sum+count
    count=count+1
print(sum,count)

# ******************************

java=86
python=68

if java >80 and python > 80:
    print("优秀")
else:
    print("不优秀")

if (java>80 and java<90) or (python>80 and python<90):
    print("良好")
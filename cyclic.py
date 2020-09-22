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
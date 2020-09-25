from turtle import *
color("red","yellow")
begin_fill()           # 开始填充图形
while True:
    forward(200)       # 向前200
    left(170)          # 向左170
    if abs(pos()) < 1: # 查看画笔是否回到原点
        break          # 如果回到，原点则跳出循环
end_fill()             # 结束填充
done()                 # 完成，页面不关闭

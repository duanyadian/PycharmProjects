for num in range(10,20):              # 迭代10~20之间的数值
    for i in range(2,num):               # 根据因子迭代
        if num%i == 0:                   # 确定第一个因子
            j = num/i                    # 计算第二个因子
            print("%d 是一个合数" %num)
            break                        # 跳出当前循环
    else:                                # 循环else部分
        print("%d 是一个质数" %num)
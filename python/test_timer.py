# 每行代码都有执行时间，大概在 数ms 左右
# 所以想要精准地控制定时器在 ms ，使用time.sleep 是不可能的
# 根据测试，几乎可以精确到 10 微妙
# 
# 另外这里是没有任何实际代码的情况
# 如果有实际运行的代码， 应当使用 线程，进程等方式执行，以避免阻塞
# 如果电脑整体负载过高，也会影响定时器的精度
import time


while True:
    print(time.time())

    #time.sleep(time.time() % 1 % 0.01)
    time.sleep(0.01)

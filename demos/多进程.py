import multiprocessing
import time
import os


def sin(num):
    # print(os.getpid())
    # print(os.getppid())
    for i in range(num):
        # time.sleep(1)
        print("唱歌......")


def dance(num):
    # print(os.getpid())
    # print(os.getppid())
    for i in range(num):
        # time.sleep(1)
        print("跳舞......")


if __name__ == '__main__':
    process1 = multiprocessing.Process(target=sin,kwargs={"num":3}, daemon = True)
    process2 = multiprocessing.Process(target=dance, kwargs={"num":3}, daemon = True)
    process1.start()
    process2.start()
    print("主进程结束")
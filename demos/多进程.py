import multiprocessing
import time
import os


def sin():
    print(os.getpid())  #获取当前进程 id
    print(os.getppid()) #获取父进程 id
    for i in range(3):
        time.sleep(1)
        print("唱歌......")


def dance():
    print(os.getpid())  # 获取当前进程 id
    print(os.getppid()) #获取父进程 id
    for i in range(3):
        time.sleep(1)
        print("跳舞......")


if __name__ == '__main__':
    process1 = multiprocessing.Process(target=sin)  #创建多进程
    process2 = multiprocessing.Process(target=dance)
    process1.start()   #启动多进程
    process2.start()
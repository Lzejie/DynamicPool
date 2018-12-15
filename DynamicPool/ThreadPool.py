# -*- coding: utf-8 -*-
# @Time    : 18/12/10 上午10:35
# @Author  : Edward
# @Site    :
# @File    : ThreadPool.py
# @Software: PyCharm Community Edition

import time

from threading import Thread


class Pool(object):
    '''
    阻塞动态线程池。
    创建完线程池后，可以动态地往里面丢任务。不用预先构建完要执行的任务，可以边执行边添加。
    '''
    def __init__(self, size=10, check_interval=0.1):
        self.workers = []
        self.worker_size = size
        # 监测时间间隔
        self.check_interval = check_interval

    # 添加一个新的任务
    def add_task(self, func, args):
        # 如果当前正在执行的线程数大于限制的数量则持续检测是否有已执行完成的线程
        while True:
            self.check_thread()
            if len(self.workers) == self.worker_size:
                time.sleep(self.check_interval)
            else:
                break

        new_thread = Thread(target=func, args=args)
        self.workers.append(new_thread)
        new_thread.start()

    # 等待任务全部执行完成
    def wait(self):
        # 当workers不为空时就一直循环，直到变为空
        while self.workers:
            self.check_thread()
            time.sleep(self.check_interval)

    # 监测是否有已经执行完的线程，如果有就删除它
    def check_thread(self):
        for index, worker in enumerate(self.workers):
            if worker.is_alive():
                continue
            else:
                print('线程 [ %s ] 已结束' % self.workers[index].name)
                del self.workers[index]


if __name__ == '__main__':
    pool = Pool(5)
    pp = lambda x: time.sleep(2) or print(x)

    for i in range(10):
        pool.add_task(pp, [i])

    pool.wait()

#!/usr/bin/env python
# coding:utf-8
# Author:Fengchunyang
"""
有序执行。有如下类OrderPrint，启动三个线程，其中线程A执行one()方法，线程B执行two()方法，线程C执行three()方法，
请在一个OrderPrint实例中通过线程实现one、two、three三个方法的按序执行。
"""
import Queue
import threading
import time


class OrderPrintQueueGet(object):
    """
    多线程的队列自带对线程的阻塞功能，当get方法未取到数据时，便会阻塞当前线程直到获取到数据
    """
    def __init__(self):
        self._q1 = Queue.Queue()
        self._q2 = Queue.Queue()
        self.order = {
            1: threading.Thread(target=self.one),
            2: threading.Thread(target=self.two),
            3: threading.Thread(target=self.three),
        }

    def one(self):
        print "one executed"
        self._q1.put(True)

    def two(self):
        self._q1.get()
        print "two executed"
        self._q2.put(True)

    def three(self):
        self._q2.get()
        print "three executed\n"

    def run(self, first, second, third):
        """根据传入的顺序，调用不同的线程"""
        self.order.get(first).start()
        self.order.get(second).start()
        self.order.get(third).start()
        return


class OrderPrintQueuePut(object):
    """
    多线程的队列自带对线程的阻塞功能，对定长队列而言，当队列已满时，也会阻塞线程，直到队列有空间入队数据
    """
    def __init__(self):
        self._q1 = Queue.Queue(1)
        self._q2 = Queue.Queue(1)

        self._q1.put(True)
        self._q2.put(True)
        self.order = {
            1: threading.Thread(target=self.one),
            2: threading.Thread(target=self.two),
            3: threading.Thread(target=self.three),
        }

    def one(self):
        print "one executed"
        self._q1.get()

    def two(self):
        self._q1.put(True)
        print "two executed"
        self._q2.get()

    def three(self):
        self._q2.put(True)
        print "three executed\n"

    def run(self, first, second, third):
        """根据传入的顺序，调用不同的线程"""
        self.order.get(first).start()
        self.order.get(second).start()
        self.order.get(third).start()
        return


class OrderPrintLock(object):
    """使用线程锁限制运行顺序"""
    def __init__(self):
        self.l1 = threading.Lock()
        self.l2 = threading.Lock()
        self.order = {
            1: threading.Thread(target=self.one),
            2: threading.Thread(target=self.two),
            3: threading.Thread(target=self.three),
        }
        self.l1.acquire()
        self.l2.acquire()

    def one(self):
        print "one executed"
        self.l1.release()  # 执行完毕后释放l1锁

    def two(self):
        self.l1.acquire()
        print "two executed"
        self.l2.release()

    def three(self):
        self.l2.acquire()
        print "three executed\n"

    def run(self, first, second, third):
        self.order.get(first).start()
        self.order.get(second).start()
        self.order.get(third).start()


class OrderPrintSemaphore(object):
    """使用信号量限制运行顺序，和线程锁类似"""
    def __init__(self):
        self.l1 = threading.Semaphore(0)
        self.l2 = threading.Semaphore(0)
        self.order = {
            1: threading.Thread(target=self.one),
            2: threading.Thread(target=self.two),
            3: threading.Thread(target=self.three),
        }

    def one(self):
        print "one executed"
        self.l1.release()

    def two(self):
        self.l1.acquire()
        print "two executed"
        self.l2.release()

    def three(self):
        self.l2.acquire()
        print "three executed\n"

    def run(self, first, second, third):
        self.order.get(first).start()
        self.order.get(second).start()
        self.order.get(third).start()


if __name__ == "__main__":
    op1 = OrderPrintSemaphore()
    op2 = OrderPrintSemaphore()
    op3 = OrderPrintSemaphore()
    op1.run(1, 3, 2)
    time.sleep(1)
    op2.run(3, 2, 1)
    time.sleep(1)
    op3.run(1, 2, 3)




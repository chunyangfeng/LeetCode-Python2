#!/usr/bin/env python
# coding:utf-8
# Author:Fengchunyang
"""
有如下类，提供foo和bar两个方法，在同一个实例中，实现对foo和bar的交叉调用，使结果形式为foobarfoobarfoobar...
"""

import threading
import Queue


class CrossPrintQueue(object):
    def __init__(self, n):
        self.n = n
        self.q1 = Queue.Queue(1)  # the queue length is 1
        self.q1.put(True)

    def foo(self):
        self.q1.get()  # when foo is called,the queue of q1 is full,it can be get
        print "foo"

    def bar(self):
        self.q1.put(True)  # if bar must be called after foo,use put method blocked this function until q1 become empty
        print "bar"

    def run(self):
        while self.n != 0:
            f = threading.Thread(target=self.foo)
            b = threading.Thread(target=self.bar)
            b.start()
            f.start()  # no matter foo or bar is called first,the output will always "foobar..."
            self.n -= 1
        return


if __name__ == '__main__':
    cpq = CrossPrintQueue(5)
    cpq.run()


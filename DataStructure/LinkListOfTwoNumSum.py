#!/usr/bin/env python
# coding:utf-8
# Author:Fengchunyang
"""
两个非空链表表示两个非负整数，其中位数是按照逆序存储，并且一个节点只存储一位数字。
请给出函数，传入两个这种链表，计算它们的和并返回新的链表。
eg: [2, 4, 3] + [5, 6, 4] = 342+465 = 807 => [7, 0, 8]
"""


def add(l1, l2):
    big = l1 if len(l1) >= len(l2) else l2
    small = l1 if len(l1) < len(l2) else l2
    while len(big) != len(small):
        small.append(0)
    r = [a + b for a, b in zip(big, small)]
    for i, n in enumerate(r):
        if n >= 10:
            r[i+1] += 1
            r[i] -= 10
    return r


def generate_listnode(num):
    """Transform the number to a list node, such as 231 ==> [1, 3, 2]"""
    return map(int, reversed(list(str(num))))


if __name__ == "__main__":
    print add(generate_listnode(342), generate_listnode(4654))

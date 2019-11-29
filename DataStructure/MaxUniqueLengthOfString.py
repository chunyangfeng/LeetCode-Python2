#!/usr/bin/env python
# coding:utf-8
# Author:Fengchunyang
"""
给定一个字符串，返回其最长连续不重复子串的长度。
eg: 'pwddegf',最长子串是degf，长度为4；aaaaa最长子串为a，长度为1;dvdf最长子串为vdf，长度为3.
"""


def max_length_of_string(s):
    r = {}  # use dict storage the string sequence
    for index, s1 in enumerate(s):  # enumerate index and sub string of s
        r[index] = s1
        for s2 in s[index+1:]:  # slice string after sequence
            if s2 in r[index]:  # when single string appeared in dict, break the circulate
                break
            else:
                r[index] += s2
    return max([len(x) for x in r.values()])


def max_length_of_string_1(s):
    if len(s) != 0:  # when s is an empty string,the max length of sub string is 0
        max_length = 0  # length record
        window = []  # sliding window
        for ss in s:
            if ss in window:
                # when single string appeared in sliding window,record the length of window and remove redundancy string
                max_length = len(window) if len(window) > max_length else max_length
                while ss in window:
                    window.pop(0)
            window.append(ss)
        # we return the length of window or length record,because when the string just have one(like 'a'),the circulate
        # didn't record the length because the iter just execute once and not enter the if statement
        return len(window) if len(window) > max_length else max_length
    else:
        return 0


if __name__ == '__main__':
    print max_length_of_string_1(" ")
    print max_length_of_string_1("")
    print max_length_of_string_1("a")
    print max_length_of_string_1("abcabcabab")
    print max_length_of_string_1("pwwkew")

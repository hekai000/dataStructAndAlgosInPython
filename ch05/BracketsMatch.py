# encoding: utf-8
# !/usr/bin/env python

'''

@author: hekai

@license: (C) Copyright 2013-2017, kylinos.

@contact: hekai@kylinos.com.cn

@software: garner

@file: BracketsMatch.py

@time: 2019/1/23 14:59

@desc:

'''
from SStack import SStack

def check_parens(text):
    parens = "()[]{}"
    open_parens = "([{"
    opposite = {")": "(", "}": "{", "]": "["}

    def parentheses(text):

        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1
    st = SStack()

    for pr, i in parentheses(text):
        if pr in open_parens:
            st.push(pr)
        elif st.pop() != opposite[pr]:
            print "Unmatching is found at", i , "for", pr
            return False
    print "All parentheses are correctly matched."
    return True

if __name__ == "__main__":
    text1 = "ni hao (1+2) [()] {[]}"
    text2 = "ni hao (1+2) [()] [{]}"
    print check_parens(text1)
    print check_parens(text2)
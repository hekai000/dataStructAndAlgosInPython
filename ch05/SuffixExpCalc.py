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

class ESStack(SStack):
    def depth(self):
        return len(self._elems)

def suf_exp_evaluator(exp):
    operators = "+-*/"
    st = ESStack()

    for x in exp:
        if x not in operators:
            st.push(float(x))
            continue
        if st.depth() < 2:
            raise SyntaxError("Short of operand(s).")

        a = st.pop()
        b = st.pop()

        if x == "+":
            c = a + b
        elif x == "-":
            c = b - a
        elif x == "*":
            c = a * b
        elif x == "/":
            c = b / a
        else:
            break

        st.push(c)
    if st.depth() == 1:
        return st.pop()
    raise SyntaxError("Extra operand(s).")

def suffix_exp_evaluator(line):
    return suf_exp_evaluator(line.split())

def suffix_exp_calculator():
    while True:
        try:
            line = raw_input("Suffix Expression:")
            if line == "end": return
            res = suffix_exp_evaluator(line)
            print res

        except Exception as ex:
            print "Error:", type(ex), ex.args
if __name__ == "__main__":
    suffix_exp_calculator()

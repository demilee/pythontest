# coding: utf-8
# 用户输入
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",  #每行后面的逗号是为了 不换行
weight = raw_input()

print "so, you're %r old, %r height, %r heavy." % (age, height, weight)
print "so, you're %s old, %s height, %s heavy." % (age, height, weight)

x = int(raw_input())
print x
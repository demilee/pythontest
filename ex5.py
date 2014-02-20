# coding: utf-8
# 更多的变量和打印
# 格式化字符串（format string）
# 字符串可以包含格式化字符 %s，这个你之前也见过的。你只要将格式化的变量放到字符串中，再紧跟着
# 一个百分号 % (percent)，再紧跟着变量名即可。唯一要注意的地方，是如果你想要在字符串中通过格式
# 化字符放入多个变量的时候，你需要将变量放到 ( ) 圆括号(parenthesis)中，而且变量之间用 , 逗号(comma)隔开。就

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74  #inches
my_weight = 180 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line in tricky, try to get it exactly right
print "If i add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

pi = 3.1415
print "%s" % pi  # the result is 3.1415  %s	字符串
print "%f" % pi  # the result is 3.141500  %f	浮点数字(用小数点符号)
print "%10.2f" % pi #表示 总共输出长度为10个字符，其中小数位2位
print "%010.2f" % pi  # 输出为0000003.14， 表示 总共输出长度为10个字符，其中小数位2位，不足10位的话就用0补足10位
print "%d" % pi  # 结果为3， %d 为整数型
print "%e" % pi
# found()函数，将小数四舍五入
print round(pi)  # the result is 3.0

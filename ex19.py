# coding: utf-8
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"	
    print "Get a blanket.\n"

print "We can just give the function munbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our scriot:"	
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)	

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#testing...
y = int(12.1)
print y

x = int(float(raw_input()))  #raw_input()返回的是字符串类型，所以如果输入小数的话，需要先转换为浮点型（float（）），然后再转换为整型（int()）
print x

cheese = int(float(raw_input('>')))
crackers = int(float(raw_input('>')))
cheese_and_crackers(cheese, crackers)
# coding: utf-8
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    
    i = i + 1
    print "Numbers now: ", numbers
    
print "The numbers: "
for num in numbers:
    print num
    
#testing
a = 0
variables = 10
use = 2
lists1 = []
while a < variables:
    print "At the top a is %d" % a
    lists1.append(a)
    
    a = a + use
    print "lists now: ", lists1

print "The lists: "
for num in lists1:
    print num
    
# use for-loop:
list2 = []
for c in range(0, 7):
    print "now c is %d" % c 
    list2.append(c)
    print "now list2 is:", list2
    
    
    
    
    
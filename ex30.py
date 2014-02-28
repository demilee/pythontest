# coding:utf-8
people = 30
cars = 30
buses = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
    print "we still can not decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "FIne, let's stay home then."

#testing
if cars > people and cars > buses:
	print "cars is nub1!"
elif cars > people and cars < buses:
    print "buses is nub1!"
else:
    print "who care!!"    	
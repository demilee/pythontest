def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
	
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
	
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, weight: %d, IQ: %d" % (age, height, weight, iq)

# A Puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "can you do it by hand?"


#testing


def add1(a, b):
    print "ADDING %.2f + %.2f" % (a, b)
    return a + b

def subtract1(a, b):
    print "SUBTRACTING %.2f - %.2f" % (a, b)
    return a - b
	
def multiply1(a, b):
    print "MULTIPLYING %.2f * %.2f" % (a, b)
    return a * b
	
def divide1(a, b):
    print "DIVIDING %.2f / %.2f" % (a, b)
    return a / b
chufa = divide1(34.0, 100)
print "chufa is ", chufa

	
result = subtract1(add1(24, (divide1(34.0, 100))), 1023)
print result




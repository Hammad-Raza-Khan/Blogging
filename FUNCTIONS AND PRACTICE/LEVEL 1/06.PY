'''
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True

NOTE: abs(num) returns the absolute value of a number
'''
#SOLUTION--

def almost_there(n):
    for num in range(1,250):
        if (n>=90 and n<=110) or (n>=190 and n<=210) :
            return True
        else :
            return False

print(almost_there(210.5))

#----------------------

#BY USING ABS FUNCTION-

def almost_there(n):
    return (abs(100-n)<=10) or (abs(200-n) <= 10)

print(almost_there(210))

    

    

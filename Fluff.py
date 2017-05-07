stack = [1]
import sys
import math
input = sys.argv[0]
results = []

def pushToStack(a):#Adds to stack
	stack.append(a)

def getFromStack():
	return (stack[0])

def getSStack(a):
	return (stack[a])
def noArgs(a):#Please don't judge. Even noArgs need a heading
        return noArgDict[a][1]()
def factorial(a):
        return math.factorial(a)
noArgDict = {
"":""



}
oneArgDict = {
"!":factorial,
"":"",
"":"",
"":"",
"":"",
"":"",
"":"",
"":"",
"":"",
"":"",
"":"",
"":"",
"":"",
}
twoArgDict = {
"^":"power",
"%":"mods",
"*":"multi",
"":"",
"":"",
"":"",
"":"",
"":"",
"":"",
}
def oneArgs(a,b):#OK IT NEEDS 2 ARGS SO WE KNOW WHAT IT IS TALKING ABOUT STOP JUDGING
	return oneArgDict[a](b)

def twoArgs(a,b,c):
	return twoArgDict[a][1](b,c)
def power(a,b):
	return a^b

def multi(a,b):
	return a*b
def mods(a,b):
        return mod(a,b)

def runRegEx():
        return 0


print(oneArgs("!",2))



#funcs = {
 #   "!": factorial,
 #   "+": float.__add__
#}

print(oneArgDict["!"](3))

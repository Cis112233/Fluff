stack = []
input = 
results
oneArgDict = {
"♂":"",#11
"♀":"",#12
"♪":"",#13...
"♫":"",
"☼":"",
"►":"",
"◄":"",
"↕":"",
"‼":"",
"§":"",
"▬":"",
"↨":"",
"↑":"",
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
def pushToStack(a):#Adds to stack
	stack.append(a)

def getFromStack():
	return (stack[0])

def getSStack(a):
	return (stack[a])

def oneArgs(a):#not added
	return 0

def twoArgs(a,b,c):
	eval(twoArgDict[a]+"("+b+c+")")
def power(a,b):
	return a^b

def multi(a,b):
	return a*b
def mods(a,b):
    return mod(a,b)

def runRegEx():
    return 0
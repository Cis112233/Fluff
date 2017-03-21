stack = []
input = sys.argv[0]
results
noArgDict = {
"":""



}
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
def noArgs(a):#Please don't judge. Even noArgs need a heading
    return noArgDict[a][1]()

def oneArgs(a,b):#OK IT NEEDS 2 ARGS SO WE KNOW WHAT IT IS TALKING ABOUT STOP JUDGING
	return oneArgDict[a][1](b)

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

#global
arraylist = list()
totalsum = 0
doublesum = 1
doublesumrecord = 0

#root programs

def testforeven():
    
    global totalsum
    global arraylist
    
    if totalsum % 2 == 0:
	    arraylist.append(totalsum)

#end root programs

#start combo programs
		
def trysolveproblem2():
	global arraylist
	global doublesumrecord
	global totalsum
	global doublesum
	
	totalsum = totalsum + doublesum
	
	doublesum = totalsum
	
	testforeven()
	
	totalsum = totalsum + doublesumrecord
	
	doublesumrecord = totalsum
	
	testforeven()

#end combo programs

#start Main program

totalsum = doublesum + totalsum
	
doublesumrecord = totalsum
	
testforeven()

while totalsum <= 4000000:
	trysolveproblem2()
	
print(sum(arraylist))

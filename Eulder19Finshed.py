"find sundays between 99 years"
"every sunday is a 7"
"daycounter is the offset of the month for the start of each month"
"daycounter starts at 1 because its monday"

#globle veribles

yearcounter = 1901
daycounter = 1
sundaycounter = 0

#root programs:

def feb():
    global yearcounter
    global daycounter
    
    if yearcounter % 4 == 0.00:
        daycounter = daycounter + 1

def dayscounter():
    global daycounter
    
    if daycounter >= 8:
        daycounter = daycounter - 7
        
def sundayscounter():
    global sundaycounter
    global daycounter
    
    if daycounter == 7:
        sundaycounter = sundaycounter + 1

def yearscounter():
    global yearcounter
    
    yearcounter = yearcounter + 1

#end root programs

#start compound programs

def e31days():
    global daycounter
    
    sundayscounter()
    daycounter = daycounter + 3
    dayscounter()
    
def e30days():
    global daycounter
    
    sundayscounter()
    daycounter = daycounter + 2
    dayscounter()
    
def Febfin():
    sundayscounter()
    feb()
    dayscounter()

#end compound programs
    
        
#main program
        

"program run"

while yearcounter <= 1999:
    e31days()
    Febfin()
    e31days()
    e30days()
    e31days()
    e30days()
    e31days()
    e31days()
    e30days()
    e31days()
    e30days()
    e31days()
    yearscounter()

print("there are")
print(sundaycounter)
print("between 1901 and 2000")

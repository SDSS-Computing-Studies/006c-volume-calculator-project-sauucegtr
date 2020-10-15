#!python3
# Volume Calculator
# Feel free to rename your variables
import math

def title():
    print("=================")
    print("This is the title.")
    print("=================")
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author:Jon
    # Modified:
    
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    print("This is to find the area of the shape")
    print("Enter in what shape you have and what the measurments are for that shape")
    return None

def getshape(shape):
    shape=input("Enter In what shape you have")

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    
    if shape=="rectangularprism":
        return["Enter Height","Enter Lenght","Enter Width"]
    elif shape=="shpere":
        return ["enter radius"]
    elif shape=="cone":
        return["Enter Height","Enter Radius"]
    elif shape=="cylander":
        return["Enter Height","Enter radius"]
    elif shape=="pyramid":
        return["enter lenght","Enter width", "enter height"]

def volumefindRectangularPrism(measurements):
    a=measurements[0]
    b=measurements[1]
    c=measurements[2]
    volume=a*b*c
    return volume

def volumefindSphere(measurements):
    a=measurements[0]
    volume= ((a**3)*math.pi)*(4/3)
    return volume

def volumefindCone(measurements):
    a=meausrments[0]
    b=measurements[1]
    volume=(a/3)*((b**2)*math.pi)
    return volume
def volumefindCylander(measurments):
    a=meausrments[0]
    b=measurements[1]
    volume=(b**2)*a*math.pi
    return volume
def volumefindPyramid(measuerments):
    a=meausrments[0]
    b=measurements[1]
    c=measurments[2]
    volume=(a*b*c)/3
    return volume


def getInputs(questions):
    print(questions)
    numInd=questions.count()
    bra=[]
    b=0
    for i in range(0,numInd):
        num1=float(input(questions[i]))
        meList.insert(i,b)
        measurements=bra

    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    # Author:Jon
    # Modified:
    measurements = []
    
    
    
    return measurements

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()
    instructions()
    ans=calc()
    ans=print("The volume of the " +str(shape)+" you specified is "+ str(ans) +" units cubed." )
    return ans
    # ask for a shape


main()

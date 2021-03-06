#!python3
# Volume Calculator
# Feel free to rename your variables
import math

def title():
    print("=================")
    print("Volume Calculater.")
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
    # Author:josh
    # Modified:
    print("This is to find the area of the shape")
    print("Enter in what shape you have and what the measurments are for that shape")
    print("The Valid shapes are rectangularprism, sphere, cone, cylander, pyramid")
    print("=================")
    return None



def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    
    if shape=="rectangularprism":
        return["Enter Height ","Enter Lenght ","Enter Width "]
    elif shape=="sphere":
        return ["Enter radius "]
    elif shape=="cone":
        return["Enter Height ","Enter Radius "]
    elif shape=="cylander":
        return["Enter Height ","Enter radius "]
    elif shape=="pyramid":
        return["Enter lenght ","Enter width ", "Enter height "]
    elif shape=="exit":
        exit()
    else: 
        print("This is not A valid Shape, Please try again. Enter 'exit' if you whish to stop")
        main()

def square(measurements):
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
    a=measurements[0]
    b=measurements[1]
    volume=(a/3)*((b**2)*math.pi)
    return volume
def volumefindCylander(measurements):
    a=measurements[0]
    b=measurements[1]
    volume=(b**2)*a*math.pi
    return volume
def volumefindPyramid (measurements):
    a=measurements[0]
    b=measurements[1]
    c=measurements[2]
    volume=(a*b*c)/3
    return volume


def getInputs(questions):
    print(questions)
    numInd=len(questions)
    measurements=[]
    for i in range(0,numInd):
        num1=float(input(questions[i]))
        
        measurements.append(num1)
        

    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    # Author:Jon
    # Modified:
    
    
    
    
    return measurements

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()
    instructions()
    shape=input("Enter In what Shape you have here ")
    # ask for a shape
    # get the questions using the shape
    # get the measurements using the questions
    x=getParams(shape)
    
    y=getInputs(x)
    

    # using shape and measurements decide which calculator to use
    if shape == "rectangularprism":
        a=square(y)
        print("The Volume Of your objects is "+ str(a))
        ending()
    elif shape=="sphere":
        a=volumefindSphere(y)
        print("The Volume Of your objects is " +str(a))
        ending()
    elif shape=="cone":
        a=volumefindCone(y)
        print("The Volume Of your objects is " +str(a))
        ending()
    elif shape=="cylander":
        a= volumefindCylander(y)
        print("The Volume Of your objects is " +str(a))
        ending()
    elif shape=="pyramid":
        a= volumefindPyramid(y)
        print("The Volume Of your objects is " +str(a))
        ending()
def ending():
        print("=================")
        a=input("Thanks for using the program, enter exit if you whish to stop, or continue to do it again ")
        
        if a=="exit":
            exit()
        elif a=="continue":
            main()
        print("=================")

main()




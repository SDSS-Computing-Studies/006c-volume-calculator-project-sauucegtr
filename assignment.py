#!python3
# Volume Calculator
# Feel free to rename your variables


def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    Print("This is find the area of the shape")
    Print("Enter in what shape you have and what the measurments are for that shape")
    return None

def getshape(shape):
    shape=input("Enter In what shape you have")

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    
    if shape=rectangle:
        return["Enter Height","Enter Lenght","Enter Width"]
    elif shape=Shpere:
        return ["enter radius"]
    elif shape=cone:
        return["Enter Height","Enter Radius"]
    elif shape=cylander:
        return["Enter Height","Enter radius"]
    elif shape=pyramid:
        return["enter lenght","Enter width", "enter height"]
    
    prompts

    return prompts

def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurements=[]
    if sh
    
    
    return measurements

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()
    instructions()


main()
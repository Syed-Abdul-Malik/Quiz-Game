import sys


print ("Hello and welcome to my Quiz Game \n")

playing = input("Do you want to start the game?" + "\t Please type 'Yes' if you want to continue. \n")

if playing.lower() != "yes":
    print("Exiting the game as you have not typed 'Yes'" + " ==>   To continue with the Quiz game please type yes")
    quit()
    
print("\nOkay then lets play :)")
score = 0

answer = input("\nwhat does CPU stand for? \n")
if answer.lower() == ("central processing unit"):
    print("\nGreat that's correct :)" )
    score +=1
    
else: 
    print("\nThat's the wrong answer:(    The correct answer is 'Central Processing Unit'")
    
answer = input("\nwhat does RAM stand for? \n")
if answer.lower() == ("random access memory"):
    print("\nGreat that's correct :)")
    score +=1

else: 
    print("\nWrong answer:(    The correct answer is 'Random Access Memory'")
    
answer = input("\nwhat does GPU stand for? \n")
if answer.lower() == ("graphics processing unit"):
    print("\nGreat that's correct :)")
    score +=1
    
else: 
    print("\nWrong answer:(    The correct answer is 'Graphics Processing Unit'")
    
    
answer = input("\nwhat does PSU stand for?\n")
if answer.lower() == ("power supply unit"):
    print("\nGreat that's correct :)")
    score +=1
    
else: 
    print("Wrong answer:(    The correct answer is 'Power Supply Unit'")
    
answer = input("\nLast Question: What is the name of the developer? \n")
if answer.lower() == ("syed abdul malik"):
    print("\nyou're correct :)" )
    score +=1
    
else: 
    print("The Developer's name is 'Syed Abdul Malik'\n")

print("\nYou have compeleted the quiz! \n" + "Your Score is " + str(score))


sys.exit()
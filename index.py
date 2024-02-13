
# Collect candidate information

numberOfCandidates = int(input("How many candidates are running in the vote? \n")) #Find out how many candidates
number = str(numberOfCandidates) #Convert variable to a string so it can concatenate in the print statement below

# Need to account for errors where people don't enter a number

print("Okay, there will be " + number + " candidates in this vote.\n") #Provide ffedback to user
print("Let's collect each candidate's name...\n") #Prompt users next input

candidate_names = list() #Create empty Python List that will stor all the str names within a single List object.

i = 0 #I could only get it to work this way, ie using a While Loop, so I have set the counter to zero
while i < numberOfCandidates:
    content = input("What is the next candidates name? ")
    candidate_names.append(content) #Using 'append' function to add each input as a value in the List
    i = i+1 #Increment the counter for the While loop
    print("Recorded & incremented\n") # Provide feedback to developer to know the Loop is looping

print(candidate_names) # Provide feedback to developer to see what's now contained in the list
    

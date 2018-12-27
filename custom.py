import pandas as pd 

##ask initialization columns.

print("what types of prompts would you like to be asked daily?")
done = False

print("press 0 when you're done.")
promptCols = []
##ask for prompts
while  not done:
	if done == True:
		break
	else:
		promptIn = input("enter a prompt: ")
		if promptIn == '0':
			done = True
			break
		promptCols.append(promptIn)


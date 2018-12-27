#!/usr/bin/env python3
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
		else:
			promptCols.append(promptIn)

print("with the prompts done, heres what happens:")
print("You're going to get prompted everday to update those prompts.")
print("you ask to see your progress, by running <INSERT PLOT.py>")

print("\n\n Lets start by prompting you first: fill out the following prompts you asked for:")
initialPromps={} 
for i in promptCols:
	initialPromps[i] = None
for k in initialPromps.keys():
	v = input(k+":\n")
	initialPromps[k]=[v]
print("great! Now theres a sample of your responses. Writing the csv now.")

init = pd.DataFrame.from_dict(initialPromps)
#init = init.drop(["Unnamed: 0"],axis=1)
#hack to remove "Unnamed Bug"
init.to_csv("data.csv")
# el = pd.read_csv("data.csv")
# el = el.drop(["Unnamed: 0"],axis=1)
# el.to_csv("data.csv")
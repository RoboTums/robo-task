#!/usr/bin/env python3
import pandas as pd 

print("Hello! Lets update!")
DF = pd.read_csv("data.csv", index_col=0)

response = []
# loop through questions
for i in DF.columns.values:
	#print out question 
	resp = input(i+":\n")

	# append response
	response.append(resp)
DF.loc[len(DF)] = response
#rewrite csv
DF.to_csv("data.csv")

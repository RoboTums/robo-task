import pandas as pd 

print("Hello! Lets update!")
DF = pd.read_csv("data.csv")

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

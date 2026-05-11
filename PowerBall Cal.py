import pandas as pd

#dataframe = df
df = pd.read_csv("/Users/legend/Downloads/Powerball_Winning_Numbers__1year.csv")

#print(df.head(52))
#df.columns["Winning Numbers"].value_counts()
#count how many times
#print(df["Winning Numbers"].value_counts())
#print selected row
#PowerBall = df["Winning Numbers"].iloc[-1]
#print(PowerBall)

#Creating a new column in a dataframe
#"""df_2 = df.assign(B=["PowerBall"]*len(df))
#print(df_2)"""
#print(df.mode["PowerBall"])
#Mode1 =df.mode()
#print(Mode1)
#print(df["Winning Number"].mode())
print(df.value_counts("Winning Number"))

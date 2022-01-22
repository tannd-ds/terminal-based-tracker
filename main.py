import numpy as np
import pandas as pd
import os

print("Write the PATH to your Data source: ")
PATH = input()
df = pd.read_csv(PATH, index_col=False)

print("Your last 5 entries: ")
print(df.tail())

def addRow(df):
    row = {}
    for col in df.columns:
        print(col + ":", end=" ")
        row[col] = input()
    return df.append(row, ignore_index=True)

def removeRow(df):
    return df.drop(axis = 1, index = len(df.index) - 1)

def saveTable(df):
    df.to_csv(PATH, index=False)

command = ""
while command != "end":
    print("Command: ", end="")
    command = input()
    if command == "add":
        df = addRow(df)
        print(df)
    elif command == "remove":
        df = removeRow(df)
        print(df)
    elif command == "save":
        print("saved!")
        saveTable(df)
    else:
        print("This is not a valid command, please try again...")



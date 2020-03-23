from random import randint
import pandas as pd

userCSV = pd.read_csv("./matric.csv")


def random_with_N_digits():
    range_start = 1
    range_end = 999999
    return randint(range_start, range_end)


matricList = []
nameList = []
passwordList = []

for index, row in userCSV.iterrows():
    nameList.insert(index, row[1])
    passwordList.insert(index, random_with_N_digits())
    matricList.insert(index, row[0])

userCSV["matric"] = matricList
userCSV["name"] = nameList
userCSV["password"] = passwordList

userCSV.to_csv('ResidentPassword.csv', sep=',')
userCSV.to_excel('ResidentPassword.xlsx')

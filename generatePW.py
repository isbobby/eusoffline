from random import randint
import pandas as pd

userCSV = pd.read_csv("./newresidents.csv")


def random_with_N_digits():
    range_start = 100000
    range_end = 999999
    return randint(range_start, range_end)


matricList = []
nameList = []
passwordList = []

for index, row in userCSV.iterrows():
    nameList.insert(index, row[0])
    passwordList.insert(index, random_with_N_digits())
    matricList.insert(index, row[1])

userCSV["matric"] = matricList
userCSV["name"] = nameList
userCSV["password"] = passwordList

userCSV.to_csv('newResidentPassword.csv', sep=',')
userCSV.to_excel('newResidentPassword.xlsx')

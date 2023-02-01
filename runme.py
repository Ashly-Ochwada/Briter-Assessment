import pandas as pd



df = pd.read_csv('original.csv', header=1)

def findDuplicates(input):
    newlist = []
    duplist = []
    for i in input:
        if i not in newlist:
            newlist.append(i)
        else:
            duplist.append(i)
    return duplist

def isNotCapital(input):
    notCapitals = []
    for i in input:
        if i[0].islower():
            notCapitals.append(i)
    return notCapitals

def onlyXxx(input):
    xxx = []
    for i in input:
        if all(c == 'x' for c in i):
            xxx.append(i)
    return xxx


dupes = findDuplicates(df.iloc[:, 0])
print(dupes)

nonCaps = isNotCapital(df.iloc[:,0])
print(nonCaps)

xxxxx = onlyXxx(df.iloc[:,2])
print(xxxxx)
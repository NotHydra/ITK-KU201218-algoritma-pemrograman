from random import sample

caseList = sample(range(1, 10), k=5)

maxValue = 0
for caseObject in caseList:
    if maxValue < caseObject:
        maxValue = caseObject

print(caseList)
print(maxValue)

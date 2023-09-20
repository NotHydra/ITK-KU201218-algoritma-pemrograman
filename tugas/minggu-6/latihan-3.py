from random import sample

caseList = sample(range(1, 10), k=5)

maxValue = caseList[0]
for caseObject in caseList[1:]:
    if maxValue < caseObject:
        maxValue = caseObject

print(caseList)
print(maxValue)

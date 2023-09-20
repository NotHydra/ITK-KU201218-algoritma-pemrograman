from random import sample

caseList = sample(range(1, 10), k=5)

minValue = caseList[0]
for caseObject in caseList[1:]:
    if minValue > caseObject:
        minValue = caseObject

print(caseList)
print(minValue)

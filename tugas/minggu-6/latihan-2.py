from random import sample

caseList = sample(range(1, 10), k=5)

total = 0
for caseObject in caseList:
    total += caseObject

print(caseList)
print(total)
print(len(caseList))
print(total / len(caseList))

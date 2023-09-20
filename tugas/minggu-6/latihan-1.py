from random import randint, sample

# caseList = [randint(1, 10) for _ in range(1, 6)]
caseList = sample(range(1, 10), k=5)

total = 1
for caseObject in caseList:
    total = total * caseObject

print(caseList)
print(total)

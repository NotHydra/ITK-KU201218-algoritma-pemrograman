from random import sample


def debug(*text, active=False):
    if active:
        print(*text)


caseList = [sample(range(1, 500), 100) for _ in range(1, 50)]

for caseObject in caseList:
    sortedList = caseObject.copy()

    while True:
        switchCount = 0

        i = 1
        while i < len(sortedList):
            debug(sortedList)

            tempPrevious = sortedList[i - 1]
            tempCurrent = sortedList[i]

            debug(i)
            debug(tempPrevious, tempCurrent)

            if tempPrevious > tempCurrent:
                sortedList[i] = tempPrevious
                sortedList[i - 1] = tempCurrent

                switchCount += 1

            debug(sortedList)
            debug()

            i += 1

        if switchCount == 0:
            break

    print(caseObject)
    print(sortedList)
    print()

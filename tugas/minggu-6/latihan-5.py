def debug(*text, active=False):
    if active:
        print(*text)


caseList = [
    {
        "input": [5, 4, 8, 7, 2, 10, 1, 6, 3, 9],
        "output": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    },
    {
        "input": [4, 3, 5, 1, 2],
        "output": [1, 2, 3, 4, 5],
    },
]

for caseDictionary in caseList:
    inputList = caseDictionary["input"].copy()

    while True:
        switchCount = 0

        i = 1
        while i < len(inputList):
            debug(inputList)

            tempPrevious = inputList[i - 1]
            tempCurrent = inputList[i]

            debug(i)
            debug(tempPrevious, tempCurrent)

            if tempPrevious > tempCurrent:
                inputList[i] = tempPrevious
                inputList[i - 1] = tempCurrent

                switchCount += 1

            debug(inputList)
            debug()

            i += 1

        # i = len(inputList) - 2
        # while i >= 0:
        #     debug(inputList)

        #     tempPrevious = inputList[i + 1]
        #     tempCurrent = inputList[i]

        #     debug(i)
        #     debug(tempPrevious, tempCurrent)

        #     if tempPrevious < tempCurrent:
        #         inputList[i + 1] = tempCurrent
        #         inputList[i] = tempPrevious

        #         switchCount += 1

        #     debug(inputList)
        #     debug()

        #     i -= 1

        if switchCount == 0:
            break

    print(
        caseDictionary["input"],
        caseDictionary["output"],
        inputList,
        caseDictionary["output"] == inputList,
    )

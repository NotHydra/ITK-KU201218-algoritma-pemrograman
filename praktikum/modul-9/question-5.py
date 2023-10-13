start = int(input())
end = int(input())


def sumOdd(start, end):
    if start % 2 == 0 and start != end:
        return start + sumOdd(start + 1, end)

    elif start != end:
        return sumOdd(start + 1, end)

    elif start % 2 == 0 and start == end:
        return start

    else:
        return 0


print(sumOdd(start, end) if end > start else sumOdd(end, start))

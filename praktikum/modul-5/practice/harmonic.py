number = int(input())

total = 1
print("1", end="")
for i in range(2, number + 1):
    print(f" + (1/{i})", end="")
    
    total += 1/i

print(f" = {total}")

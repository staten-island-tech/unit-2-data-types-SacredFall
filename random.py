def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum


lst = [x for x in range(1, 2024) if x % 3 == 0]

result = map(getSum, lst)

print(len(list(result)))
print(result)



n = int(input("enter the number"))
str = "Janani How are you".replace(" ", "")
i = 0
while i <= len(str):
    print(str[i: i+n], end= " ")
    i += n
first = 0
second = 1
res = ""
print()
test = "apple"
while second < len(test):
    res += test[second]
    res += test[first]
    first += 2
    second += 2
print(res)



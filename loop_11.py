num = int(input("Enter a number: "))
count = 0

for digit in str(abs(num)):
    count = count + 1

print("Number of digits =", count)
text = input("Enter a string: ")
words = text.split()
count = 0

for word in words:
    count = count + 1

print("Total words =", count)
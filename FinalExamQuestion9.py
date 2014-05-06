SENTINEL = "quit"
total  = 0
count = 0

entry = input("Enter a numeric value or type " + SENTINEL + " to quit: ")
while entry != SENTINEL:
    total += int(entry)
    count += 1
    entry = input("Enter a numeric value or type " + SENTINEL + " to quit: ")
print("Total of entries: ", total, "\nAverage input value: ", (total / count))

number = int(input("Enter the number of ribbons: "))


def classify(value):
    if value < 78:
        return "Below range"
    elif value <= 82:
        return "In range"
    else:
        return "Above range"

def calculate_average(total, count):
    return total / count

total = 0
below = 0
in_range = 0
above = 0

for i in range(number):

    length = int(input("Enter the ribbon length: "))

    solve = classify(length)
    print(solve)

    total = total + length

    if solve == "Below range":
        below = below + 1
    elif solve == "In range":
        in_range = in_range + 1
    else:
        above = above + 1

average = calculate_average(total, number)
print(f"Total length: {total}")
print(f"Average length: {average}")
print(f"Below range: {below}")
print(f"In range: {in_range}")   
print(f"Above range: {above}")
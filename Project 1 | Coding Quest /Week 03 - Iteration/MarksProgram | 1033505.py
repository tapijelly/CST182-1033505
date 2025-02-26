nums = []
count = 1
marks = 0  

while True:
    mark = int(input(f"Mark #{count}? "))
    if mark < 0:
        break
    nums.append(mark) 
    count += 1
    marks += 1  

if marks == 0:
    print("No marks entered.")
else:
    highest = nums[0]
    lowest = nums[0]
    total = 0

    for mark in nums:
        if mark > highest:
            highest = mark
        if mark < lowest:
            lowest = mark
        total += mark

    average = total / marks

    print("Number of marks =", marks)
    print("Highest Mark =", highest)
    print("Lowest Mark =", lowest)
    print("Average Mark =", round(average, 1))

num = int(input("Enter an interger: "))
sum = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        sum += i

print(f"Sum of even numbers from 1 to {num} is {sum}")
 

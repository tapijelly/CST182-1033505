one = int(input('Number 1? '))
two = int(input('Number 2? '))
three = int(input('Number 3? '))

low, medium, high = 0,0,0

if one < two:
    low = one
    high = two
else: 
    high = one
    low = two

if high > three:
    medium = three
else:
    medium = high
    high = three

if low > medium:
    low, medium = medium, low

print('Result =',low, medium, high)

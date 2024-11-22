my_numbers = [10, 20, 30, 40, 50]

for i in range(4):
    my_numbers.insert(i, my_numbers[-1])

print(my_numbers)


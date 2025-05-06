import time 
my_list = [1, 2, 3, 4]
my_squares = []

for i in my_list:
    time.sleep(1)
    squared = i**2
    my_squares.append(squared)

print(my_squares)
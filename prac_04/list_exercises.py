number_of_numbers = 5
list_of_numbers = []

for i in range(1,number_of_numbers+1):
    number = int(input('enter number:'))
    list_of_numbers.append(number)
print(list_of_numbers)
print(f'The first number is {list_of_numbers[0]}')
print(f'The last number is {list_of_numbers[-1]}')
print(f'The smallest number is {min(list_of_numbers)}')
print(f'The largest number is {max(list_of_numbers)}')
print(f'The average of the numbers is {(sum(list_of_numbers)/len(list_of_numbers))}')



##1
name_output = open("name.txt", 'w')
name = str((input('Enter your name:')))
print('Hello ' + name)
name_output.write(name)
name_output.close()


##2
name_input = open("name.txt", 'r')
print('Your name is ' + name_input.read())
name_input.close()

##3
numbers_input = open('numbers.txt')
numlines = 2
total = 0
for i in range(numlines):
    j = int(numbers_input.readline())
    total = total+j
print(total)
numbers_input.close()


##4
numbers_input = open('numbers.txt')
numbers = numbers_input.readlines()
numbers = [numbers.rstrip() for numbers in numbers]
ints = [int(item) for item in numbers]
print(sum(ints))
numbers_input.close()


import random

number_of_tickets = int(input('How many tickets would you like?'))
list_of_tickets = []

for i in range(1, number_of_tickets+1):
    numbers = list(range(1, 51))
    random.shuffle(numbers)
    ticket = numbers[:6]
    print(ticket)
    list_of_tickets.append(ticket)

string = str(input("Enter text: "))

string_split = string.split()

string_dict = dict((x,string_split.count(x)) for x in set(string_split))

strings = sorted(string_dict.items())



print(strings)

for i in range(0,len(strings)-1):
    print(f'{strings[i][0]}: {strings[i][1]:>10}')
### this was hard to do because I am so used to using packages like regex


def main():
    emaildict = {}
    email = 1
    while email != '':
        email = str(input('Email:'))
        if not '@' in email and email != '':
            print('Please enter a valid email address')
            email = str(input('Email:'))

        specialchars = "@_.-"

        ##thought about trying to use a dict to split spec chars
        #SpecCharDict = {}
        #for i in range(0,len(specialchars)):
        #    SpecCharDict[specialchars[i]] = i

        #print(SpecCharDict)

        def split_multi_delims(string: str, delims: str):
        ##splits by multiple deliminators
            if len(delims) == 0:
                return([string])

            string_split = string.split(delims[0])

            final_string = []
            for i in string_split:
                temp_string = split_multi_delims(i, delims[1:])
                final_string.extend(temp_string)
            return(final_string)

        name = split_multi_delims(email, specialchars)

        if len(name) > 1:
            name = f'{name[0]} {name[1]}'.title()
        else:
            name = f'{name[0]}'.title()

        if not email == '':
         confirm = input(f'Is the name {name}? (Y/N)').lower().strip()

        if not confirm == 'y' or confirm == '':
            name = input("Name:")


        emaildict[name.title()]= email

    for i, j in emaildict.items():
        print(f'{i:<6} {j:>10}')




main()
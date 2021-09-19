MIN_LENGTH = 2
def main():
    get_password()


def get_password():
    password = input('Set Password:')
    confirm = False
    while confirm == False:
        if len(password) < MIN_LENGTH:
            print('Please enter password of appropriate length.')
            password = input('Set Password:')
        else:
            for i in range(0, len(password)):
                print('*', end=' ')
            confirm = True


main()

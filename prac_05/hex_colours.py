CODE_TO_COLOUR = {
'cadetblue': '5f9ea0',
'cadetblue1': '98f5ff',
'cadetblue2': '8ee5ee',
'cadetblue3': '7ac5cd',
'cadetblue4': '53868b',
'chartreuse1': '7fff00',
'chartreuse2': '76ee00',
'chartreuse3': '66cd00',
'chartreuse4': '458b00',
'darkslategray3': '79cdcd'
}
print(CODE_TO_COLOUR)

colour_name = input("Enter Colour Name: ").lower()
while colour_name != "":
    if colour_name in CODE_TO_COLOUR:
        print('The Colour code for ', colour_name, "is", CODE_TO_COLOUR[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter Colour Name: ").lower()
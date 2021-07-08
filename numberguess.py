number =7

while True:

    user_input=input("Do u want to play (Y/n)").lower()

    if user_input == "n":
        break

    user_number =int(input('guess the number:'))

    if user_number == number:
        print('u win')
    elif abs(number-user_number) == 1:
        print(' close by one ')
    else:
        print('lost')

# Menu program
# data var
list_day = '1. Monday', '2. Tuesday', '3. Wednesday', '4. Thursday', '5. Friday',


# process
def main():     # main function
    print('Week day schedule.')
    for days in list_day:       # print days in list
        print(days)
    print()
    sel_day = input('Enter number for day schedule: ')      # get day
    print()
    if sel_day == '1':      # day = Monday
        monday()        # output days schedule
        cont_days()     # option to continue
    elif sel_day == '2':    # day = Tuesday
        tuesday()
        cont_days()
    elif sel_day == '3':    # day = Wednesday
        wednesday()
        cont_days()
    elif sel_day == '4':    # day = Thursday
        thursday()
        cont_days()
    elif sel_day == '5':    # day = Friday
        friday()
        cont_days()
    else:       # if input is not defined
        print('Enter a valid option.')
        print()
        main()      # return to main


def monday():       # func for monday schedule
    print('Monday Schedule:')
    print('Gym @ 9:00 am')
    print('Job Interview @ 4:00 pm')
    print()


def tuesday():      # func for tuesday schedule
    print('Tuesday Schedule:')
    print('Gym @ 9:00 am')
    print('Lunch with Arty @ 12:30 pm')
    print('Gym @ 6:00 pm')
    print()


def wednesday():        # func for wednesday schedule
    print('Wednesday Schedule:')
    print('Break day')
    print('House showing @ 12:00 pm')
    print('Dr.Dug @ 5:00 pm')
    print()


def thursday():     # func for thursday schedule
    print('Thursday Schedule:')
    print('Gym @ 9:00 am')
    print('Car maintenance @ 11:00 am')
    print('Pick up dinner for Friday')
    print()


def friday():       # func for friday schedule
    print('Friday Schedule:')
    print('Gym @ 9:00 am')
    print('Gym @ 4:00 pm')
    print('Dinner with Parks @ 6:00 pm')
    print()


def cont_days():        # function to continue or end program
    cont_progress = input('Do you want to select another day? \'y or n\': ')        # get continue
    print()
    if cont_progress == 'y':        # continue to main
        main()
    elif cont_progress == 'n':      # end program
        print('End of program.')
    else:       # if input is not defined
        print('Enter valid input.')
        cont_days()     # re-enter option


main()      # run main

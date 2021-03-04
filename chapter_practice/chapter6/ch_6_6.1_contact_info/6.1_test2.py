# Contact information intake & file

def main():
    try:
        file_info_builder = open('contact_info.txt', 'a')
        file_quantity = int(input('Number of entries: '))
        files = file_quantity

        for num in range(files):
            print('Employee: ' + str(num + 1) + ' contact entry.')
            name = input('Enter name: ')
            phone = input('Enter phone number: ')
            email = input('Enter email: ')
            file_info_builder.write(name + ', ' + phone + ', ' + email + '\n')
            print()
    except ValueError:
        print('Please input valid entry.')
        print()
        main()

        file_info_builder.close()


main()

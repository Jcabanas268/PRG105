"""
Append contact information: name, phone number, and email; to contact_info.txt
"""


def main():                                                             # define main()
    try:                                                                # process try
        file_info_builder = open('contact_info.txt', 'a')               # open text document
        print('Update contact information.')                            # prompt intro
        file_quantity = int(input('Enter number of contacts: '))        # get number of entries
        files = file_quantity                                           # number of files
        for num in range(files):                                        # iterate for number of entries
            print('Contact: ' + str(num + 1))                           # prompt select employee
            name = input('Enter name: ')                                # get name
            phone = input('Enter phone number: ')                       # get phone number
            email = input('Enter email: ')                              # get email
            file_info_builder.write(name + ', ' + phone + ', ' + email + '\n')      # update contact_info.txt
            print()                                                     # add blank line
        file_info_builder.close()
        print('Update complete.')
    except ValueError:                                                  # process except for try error
        print('Please input valid entry.')                              # prompt for valid entry
        print()                                                         # add black line
        main()                                                          # cycle to main()


main()                                                                  # call main()

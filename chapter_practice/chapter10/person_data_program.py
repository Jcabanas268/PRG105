"""
PersonData Program: creates a class for PersonData defining set and get for
persons information (name, address, age, phone). Assign contact_info to
class info. Printing information from contact_info list.
"""


class PersonData:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone


def main():
    contact_info = {'Kayla': ['755 Main St', 23, '850-923-2254'],
                    'Aron': ['882 Mill St', 31, '815-622-9845'],
                    'Kerry': ['135 Dean Dr', 28, '815-602-7646']}
    print('Person Information')
    print()
    for key in contact_info:
        p_name = key
        p_address = contact_info[key][0]
        p_age = contact_info[key][1]
        p_phone = contact_info[key][2]
        pers_data = PersonData(p_name, p_address, p_age, p_phone)
        print('Name:', pers_data.get_name())
        print('Address:', pers_data.get_address())
        print('Age:', pers_data.get_age())
        print('Phone:', pers_data.get_phone())
        print()


main()

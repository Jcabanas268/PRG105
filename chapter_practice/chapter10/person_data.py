

class Person_Data:
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
    p_name = input('Enter name: ')
    p_address = input('Enter address: ')
    p_age = int(input('Enter age: '))
    p_phone = input('Enter phone: ')

    pers_data = Person_Data(p_name, p_address, p_age, p_phone)

    print('Name:', pers_data.get_name())
    print('Address:', pers_data.get_address())
    print('Age:', pers_data.get_age())
    print('Phone:', pers_data.get_phone())


main()

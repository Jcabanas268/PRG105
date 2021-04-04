"""
program opens account document and overdue document
read document lines and compare similar values
similar values displays account as overdue
"""


def main():
    try:
        print("The following accounts are at least 90 days overdue:\n")
        file_doc_account = open('accounts.txt', 'r')
        file_doc_over90 = open('over90.txt', 'r')
        read_lines_account = file_doc_account.readlines()
        read_lines_over90 = file_doc_over90.readlines()
        for acc in read_lines_account:
            account_split = (acc.split())[0]
            account_id = account_split.rstrip(",")
            for ovrd in read_lines_over90:
                orverdue = ovrd.rstrip("\n")
                if account_id == orverdue:
                    print(acc)
    except Exception as err:
        print("Error: ", err)


main()

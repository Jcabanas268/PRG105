"""
program accumulates rainfall per month to total rainfall for twelve months.
"""


def main():             # define main()
    try:                # try run
        file_doc = open('rainfall-totals.txt', 'r')     # open readable txt file
        read_lines = file_doc.readlines()               # read lines of file
        total_rainfall = 0          # rain accumulator
        whole_place = 0             # whole number value
        dec_place = 0               # decimal number value
        non_val_error = ""          # error month and rain value
        month_count = 0             # value month
        print("Rainfall Per Month")                 # prompt title
        print("- - - " * 3)                         # display
        for ln in read_lines:                       # for read lines of file
            ln_rstrip = ln.rstrip("\n")                         # rstrip("\n")
            ln_month_value = (ln_rstrip.split())[0]             # split and index value month
            ln_rain_value = (ln_rstrip.split())[1]              # split and index value rain
            ln_rain_value_split = ln_rain_value.split(".")      # split rain by "."
            if float(ln_rain_value_split[0].isdigit()) and float(ln_rain_value_split[1].isdigit()):
                print(ln_month_value + ": " + ln_rain_value)    # if rain value whole number and decimal .isdigit()
                month_count += 1                                # display month and rain value, +1 value to month
                whole_place += float(ln_rain_value_split[0])    # add float value to whole number
                dec_place += float(ln_rain_value_split[1])      # add float value to decimal number
                total_rainfall = whole_place + dec_place / 10   # sum of whole number + decimal number / by tenth
            else:
                non_val_error += ("Error! " + ln_month_value + ": " + ln_rain_value + " value is invalid.\n")
        print("\n")                                             # compile error month and rain value
        print("- - - " * 6)                                     # display
        print(non_val_error + "\n")                             # display error month and rain value
        print("Total rainfall for " + str(month_count) + " months: " + format(total_rainfall, ',.1f') + "\n")
                    # display count for month and rainfall
        print("Average rainfall for " + str(month_count) + " months: "
              + format((total_rainfall / month_count), ',.1f') + "\n\n")
                    # display average for month and rainfall
        print("- - - " * 6)
    except Exception as err:        # except Error
        print("Error: ", err)       # display Error message
        main()                      # call main()


main()              # call main()

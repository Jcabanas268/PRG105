# credit_score

# processing
in_credit = float(input('Enter your credit score here'))        # get credit score float
if 720 < in_credit < 850:                                       # if in range 720 - 850
    print('Excellent credit score')                             # output score val excellent
    if 690 < in_credit < 719:                                   # if in range 690 - 719
        print('Good credit score')                              # output score val good
        if 630 < in_credit < 689:                               # if in range 630 - 689
            print('Fair credit score')                          # output score val fair
else:                                                           # if in range of 629 or less
    print('Bad credit score')                                   # output score val bad

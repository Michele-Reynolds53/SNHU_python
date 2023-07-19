# *************************************************************************** #
#  Michele Reynolds                                                           #
#  IT-140 - J6840  	                                                          #
#  3.12 LAB: Seasons                                                          #
#  July 14, 2023                                                               #
#  Write a program that takes a date as input and outputs the date's season.  #
# *************************************************************************** #

# Create variables to store month and day
month = input()
day = int(input())

#############################################
# March 20 through June 20 is Spring        #
# June 21 through September 21 is Summer    #
# September 22 through December 20 is Fall  #
# December 21 through March 19 is Winter    #
#############################################

if (month == "March" and 20 <= day <= 31) or (month == "April") or (month == "May") \
        or (month == "June" and 1 <= day <= 20):
    print("Spring")
elif (month == "June" and 21 <= day <= 30) or (month == "July") or (month == "August") \
        or (month == "September" and 1 <= day <= 21):
    print("Summer")
elif (month == "September" and 22 <= day <= 30) or (month == "October") or (month == "November") \
        or (month == "December" and 1 <= day <= 20):
    print("Autumn")
elif (month == "December" and 21 <= day <= 31) or (month == "January")  \
        or (month == "February" and 1 <= day <= 29) or (month == "March" and 1 <= day <= 19):
    print("Winter")
else:
    print("Invalid")
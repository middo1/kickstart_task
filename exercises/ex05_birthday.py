months = ("January" , "February" , "March" , "April" , "May" , "June" , "July" , "August" , "September" , "October" , "November" , "December")

birth_date = input("Enter birthdate in dd-mm-yyyy format: ")
month = int(birth_date[3:5])
print("Your birth month is", months[month - 1])

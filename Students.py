while True:   # while loop for repeating the questions
        last_name=input("Enter student last name: ") # will ask the user to enter last name of the student
        if last_name=="ZZZ":   # if the user entered ZZZ the program will quit and print "thank you bye!"
            print("Thank you bye!")
            break
        
        first_name=input("Enter student first name: ")  # will ask the user to enter the first name
        
        gpa=float(input("Enter student GPA: "))  # will ask user to enter the GPA of the student
        
        if gpa >= 3.5 and gpa <= 4:  # if the GPA is between 3.5 to the highest(4) the program will print " the student has made the Dean's list"
            print(first_name+" "+last_name+" has made the Dean's List.\n")
            
        elif gpa >= 3.25 and gpa <3.5: # if the GPA is between 3.25 to 3.5 , the program will print " the student has mad the Honor Roll"
            print(first_name+" "+last_name+" has made the Honor Roll.\n")
            
        elif gpa >4 or gpa <=0: # if the GPA is not in the range (less than 0 or greater than 4, the program will print "Incorrect GPA number ")
            print("Incorrect GPA number!.\n")
            
        else:
            print("Sorry "+first_name+" "+last_name+" has NOT made the Dean's List or the Honor Roll.\n") # if the student has not passed (less than 3.25), will print " the student not made the dean list or honor roll"
     


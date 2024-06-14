# Match using function

def mark(grade):

    match grade:
        case "a":
            print("Your mark range from 90 <> 100")
        case "b":
            print("Your mark range from 80 <> 89")
        case "c":
            print("Your mark range from 70 <> 79")
        case "d":
            print("Your mark range from 60 <> 69")
        case "e":
            print("Your mark range from 50 <> 59")
        case _:
            print("Not Valid Grade")

grade = input("Enter your grade:")
grade = grade.lower()
mark(grade)


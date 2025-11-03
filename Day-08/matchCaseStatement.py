def weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" |"Tuesday" |"Wednesday"|"Thrusday"|"Friday":
            return False
        case _:
            return False

print(weekend("Sunday"))
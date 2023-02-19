
def is_leap(year):
    year = leap
   
    if year % 4 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 400 == 0:
        return True
    else:
        return False    
    # Write your logic here
    return leap


print(is_leap(year))
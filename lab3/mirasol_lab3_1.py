"""
Laboratory Exercise #1
STRING MANIPULATION
"""


# do not change the function signature
def format_date(input_date:str) -> str:
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    input_date = input_date.strip()
    # blank date
    if not input_date:
        return "Invalid date format."

    try: 

        # (dmy) day month, year       ->      month day, year
        if "," in input_date:
            f_date = _dmy(input_date, months)
        # (iso) yyyy-mm-dd            ->      month day, year
        elif "-" in input_date:
            f_date = _iso(input_date, months)
        # (usa) mm/dd/yyyy            ->      month day, year
        elif "/" in input_date:
            f_date = _usa(input_date, months)
        # (eur) dd.mm.yyyy            ->      month day, year
        elif "." in input_date:
            f_date = _eur(input_date, months)
        # (others)                    ->      month day, year
        else:
            # year month day          ->      month day, year
            # yyyymmdd                ->      month day, year
            f_date = _others(input_date, months)

    except ValueError:
        return "Invalid date format."
    except TypeError:
        return "Invalid input data type."
    except KeyboardInterrupt:
        return "Exits program."
    except Exception:
        return "An unexpected error occurred."
    return f_date
    
    
# (dmy) day month, year       ->      month day, year
def _dmy(input_date:str, months:list) -> str:
    date = input_date.replace(",", " ").split(" ")
    fields = [field.strip() for field in date if field != ""]
    # incomplete date
    if len(fields) != 3:
        return "Incomplete DMY format or Invalid date format."
    # invalid year
    if len(fields[2]) > 4:
        return "Invalid DMY year."

    try:
        # MDY -> MDY
        if (fields[0].title() in months): # valid month
            if (int(fields[1]) < 32 and int(fields[1]) > 0): # valid day
                return f"{fields[0].title()} {fields[1]:0>2}, {int(fields[2])}"
            return "Invalid MDY day."
        # DMY -> MDY
        elif (fields[1].title() in months): # valid month
            if (int(fields[0]) < 32) and (int(fields[0]) > 0): # valid day
                return f"{fields[1].title()} {int(fields[0]):0>2}, {int(fields[2])}"
            return "Invalid DMY day."
        # invalid month 
        else:
            return "Invalid DMY month."

    except IndexError:
        return "Incomplete DMY format or Invalid date format."


# (iso) yyyy-mm-dd            ->      month day, year
def _iso(input_date:str, months:list) -> str:
    date = [d.strip() for d in input_date.split("-") if d != ""]
    # incomplete date
    if len(date) != 3:
        return "Incomplete ISO format or Invalid date format."
    # invalid year
    if len(date[0].strip()) > 4: # year len
        return "Invalid ISO year."

    try:

        fields = []
        for i, field in enumerate(date):
            field = int(field.strip())
            if i == 1:
                field = months[field-1]
            fields.append(field)
        # valid day 
        if (fields[2] < 32) and (fields[2] > 0):
            return f"{fields[1]} {fields[2]:0>2}, {fields[0]}"
        # invalid day 
        return "Invalid ISO day."

    except IndexError:
        return "Invalid ISO month."
    

# (usa) mm/dd/yyyy            ->      month day, year
def _usa(input_date:str, months:list) -> str:
    date = [d.strip() for d in input_date.split("/") if d != ""]
    # incomplete date
    if len(date) != 3:
        return "Incomplete USA format or Invalid date format."
    # invalid year
    if len(date[2].strip()) > 4: # year len
        return "Invalid USA year."

    try:
    
        fields = []
        for i, field in enumerate(date):
            field = int(field.strip())
            if i == 0:
                field = months[field-1]
            fields.append(field)
        # valid day 
        if (fields[1] < 32) and (fields[1] > 0):
            return f"{fields[0]} {fields[1]:0>2}, {fields[2]}"
        # invalid day 
        return "Invalid USA day."

    except IndexError:
        return "Invalid USA month."

    
# (eur) dd.mm.yyyy            ->      month day, year
def _eur(input_date:str, months:list) -> str:
    date = [d.strip() for d in input_date.split(".") if d != ""]
    # incomplete date
    if len(date) != 3:
        return "Incomplete EUR format or Invalid date format."
    # invalid year
    if len(date[2].strip()) > 4: # year len
        return "Invalid EUR year."
    
    try:
    
        fields = []
        for i, field in enumerate(date):
            field = int(field.strip())
            if i == 1:
                field = months[field-1]
            fields.append(field)
        # valid day 
        if (fields[0] < 32) and (fields[0] > 0):
            return f"{fields[1]} {fields[0]:0>2}, {fields[2]}"
        # invalid day 
        return "Invalid EUR day."

    except IndexError:
        return "Invalid EUR month."

    
# check if its 'ymd' or 'jis' w/ spaces in between
def _others(input_date:str, months:list) -> str:
    date = input_date.split(" ")
    fields = [field.strip() for field in date if field != ""]
    if len(fields) > 1: # if (ymd) year month day (w/ spaces)
        if len(fields[1]) > 2: # check if month str is a word or 1 to 2-digit num
            f_date = __ymd(fields, months)
            return f_date
    # (jis) yyyymmdd              ->      month day, year
    f_date = __jis("".join(fields), months) 
    return f_date

    
# (ymd) year month day        ->      month day, year
def __ymd(fields:list, months:list) -> str:
    # incomplete date
    if len(fields) != 3:
        return "Incomplete YMD format or Invalid date format."
    # invalid year
    if len(fields[0].strip()) > 4: # year len
        return "Invalid YMD year."
    # invalid month
    if fields[1].title() not in months:
        return "Invalid YMD month."
    
    try:
        # valid day 
        if (int(fields[2]) < 32) and (int(fields[2]) > 0):
            return f"{fields[1].title()} {int(fields[2]):0>2}, {int(fields[0])}"
        # invalid year
        return "Invalid YMD day."

    except IndexError:
        return "Invalid YMD month."


# (jis) yyyymmdd              ->      month day, year
def __jis(date:str, months:list) -> str:
    # invalid date len
    if len(date) != 8:
        return "Invalid date format."
    
    try:
    
        fields = [date[0:4], months[int(date[4:6])-1], date[6:]]
        # valid day
        if (int(fields[2]) < 32) and (int(fields[2]) > 0): # year len
            return f"{fields[1]} {int(fields[2]):0>2}, {int(fields[0])}"
        # invalid day
        return "Invalid JIS day."

    except IndexError:
        return "Invalid JIS month."


if __name__ == "__main__":
    try:

        print()
        while True:
            print("="*50)
            input_date = input("Enter date:\t")
            print("="*50)
            f_date = format_date(input_date)
            print(f"MDY date:\t{f_date}")
            print("="*50)
            choice = input("Do you want to quit (Y/N)? ").upper()
            print("="*50)
            if choice == "Y":
                break
            print(" "*23 + "*"*4)
        print()

    except KeyboardInterrupt:
        print("\nExits program.")
        print("="*50)
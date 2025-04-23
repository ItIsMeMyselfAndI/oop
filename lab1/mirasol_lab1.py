"""
Laboratory Exercise #1
STRING MANIPULATION
"""

# (dmy) day month, year       ->      month day, year
def _dmy(input_date:str) -> str:
    date = input_date.replace(",", " ").split(" ")
    fields = [field.strip() for field in date if field != ""]
    return f"{fields[1]} {fields[0]:0>2}, {fields[2]}"


# (iso) yyyy-mm-dd            ->      month day, year
def _iso(input_date:str, months:list) -> str:
    date = input_date.split("-")
    fields = []
    for i, field in enumerate(date):
        if i == 1:
            month = int(float((field.strip())))
            field = months[month-1]
        fields.append(field.strip())
    return f"{fields[1]} {fields[2]:0>2}, {fields[0]}"


# (usa) mm/dd/yyyy            ->      month day, year
def _usa(input_date:str, months:list) -> str:
    date = input_date.split("/")
    fields = []
    for i, field in enumerate(date):
        if i == 0:
            month = int(float((field.strip())))
            field = months[month-1]
        fields.append(field.strip())
    return f"{fields[0]} {fields[1]:0>2}, {fields[2]}"


# (eur) dd.mm.yyyy            ->      month day, year
def _eur(input_date:str, months:list) -> str:
    date = input_date.split(".")
    fields = []
    for i, field in enumerate(date):
        if i == 1:
            month = int(float((field.strip())))
            field = months[month-1]
        fields.append(field.strip())
    return f"{fields[1]} {fields[0]:0>2}, {fields[2]}"


# check if its 'ymd' or 'jis' w/ spaces in between
def _others(input_date:str, months:list) -> str:
    date = input_date.split(" ")
    fields = [field.strip() for field in date if field != ""]
    # (ymd) year month day        ->      month day, year
    if len(fields) > 1:
        # check if month is a word or a num
        if len(fields[1]) > 2:
            f_date = __ymd(" ".join(fields))
            return f_date
    # (jis) yyyymmdd              ->      month day, year
    f_date = __jis("".join(fields), months) 
    return f_date
# (ymd) year month day        ->      month day, year
def __ymd(date:str) -> str:
    date = date.split(" ")
    fields = [field.strip() for field in date if field != ""]
    return f"{fields[1]} {fields[2]:0>2}, {fields[0]}"
# (jis) yyyymmdd              ->      month day, year
def __jis(date:str, months:list) -> str:
    date = date
    fields = [date[0:4], months[int(date[4:6])-1], date[6:8]]
    return f"{fields[1]} {fields[2]:0>2}, {fields[0]}"


# do not change the function signature
def format_date(input_date:str) -> str:
    input_date = input_date.strip()
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    # (dmy) day month, year       ->      month day, year
    if "," in input_date:
        f_date = _dmy(input_date)
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

    return f_date.title()

if __name__ == "__main__":
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
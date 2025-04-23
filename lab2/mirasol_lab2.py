import re

"""
Laboratory Exercise #2
FILE HANDLING
"""

# do not change the function signature
def parse_data(input_file:str, names:list)->str:
    # read input file contents
    with open(input_file, "r") as input_csv:
        lines = input_csv.readlines()
    # filter rows & get output filename
    filtered_rows, output_file = _getOutputFilenameAndFilteredRows(lines, names)
    # format details
    formatted_details = _formatDetails(filtered_rows)
    # create & append output file content
    _updateOutputFile(formatted_details, output_file)
    return output_file

def _getOutputFilenameAndFilteredRows(lines:list, names:list)->tuple[list, str]:
    output_file = ".\\output"
    filtered_rows = []
    for name in names:
        name = name.upper()
        for line in lines:
            cols = line.split(",")
            if (cols[1] in name): # match last name
                for field in name.split(" "):
                    if field in cols[2]: # match at one of the multi first names
                        filtered_rows.append(line.split(","))
                        output_file += f"_{cols[1].lower()}" # add surname to output filename
                        break
    output_file += ".txt"
    return (filtered_rows, output_file)

def _formatDetails(filtered_rows:list)->str:
    formatted_details = ""    
    for line in filtered_rows:
        formatted_details += (
            f"Full name: {line[2].title()} {line[3][:1].title()}. {line[1].title()}\n"
            f"Student number: {line[0]}\n"
            f"Email address: {line[6]}\n\n"
        )
    return formatted_details

def _updateOutputFile(formatted_details:str, output_file:str)->None:
    # write output file contents 
    with open(output_file, "w") as output_txt:
        output_txt.write(formatted_details)
    # read cool_man file contents
    with open("cool_man.txt", "r") as text:
        cool_man = text.read()
    # append cool_man file contents 
    with open(output_file, "a") as output_txt:
        output_txt.write(cool_man)


################################################################################


def bonus(input_file:str, output_file:str):
    pattern = re.compile(",S\\w+O,J\\w+O")
    lines = {}
    # filter rows
    with open(input_file, "r") as input_txt:
        for i, line in enumerate(input_txt):
            if pattern.search(line):
                lines[i+1] = line
    # update output file contents
    if not lines:
        return
    with open(output_file, "a") as output_txt:
        output_txt.write("\n\n")
        for i, line in lines.items():
            output_txt.write(f"Found at line {i}: {line}")


################################################################################


if __name__ == "__main__":
    # if you are working as solo, a pair, or a group of three, add your name/s in the list
    # example: names = ['Jose Rizal', 'Taylor Swift', 'Leonardo da Vinci']

    names = ["Eger Mirasol"]
    # specify the name of the input file (e.g., BSCPE1-3.csv)
    input_file = ".\\BSCPE1-5.csv"
    output_file = parse_data(input_file, names)
    print(output_file)

    # this is for bonus item only
    bonus(input_file, output_file)


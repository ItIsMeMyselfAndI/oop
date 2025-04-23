"""
Laboratory Exercise #2
FILE HANDLING
"""

import re


# do not change the function signature
def parse_data(input_file:str, names:list)->str:
    try:
    
        # read input file contents
        lines = _getInputCSVlines(input_file)
        if lines:
            # filter rows & get output filename
            filtered_rows, output_file = _getOutputFilenameAndFilteredRows(lines, names, input_file)
            # format details
            formatted_details = _formatDetails(filtered_rows)
            # create & append output file content
            _updateOutputFile(formatted_details, output_file)
        else:
            output_file = None
    
    except KeyboardInterrupt:
        print("Parser: Exiting program...")
        print("="*50)
        exit(0)
    except Exception:
        print("Parser: an unexpected error occurred.")
        print("="*50)
        exit(0)
    return output_file


def _getInputCSVlines(input_file)->list:
    try:
        with open(input_file, "r") as input_csv:
            lines = input_csv.readlines()
    except FileNotFoundError:
        print(f"Parser: <{input_file}> is not in the current directory.")
        lines = None 
    except PermissionError:
        print(f"Parser: <{input_file}> is open in another process")
        print(f"{"":<7}    or unavailable for the user.")
        lines = None 
    return lines


def _getOutputFilenameAndFilteredRows(lines:list, names:list, input_file:str)->tuple[list, str]:
    output_file = ".\\output"
    filtered_rows = []
    for name in names:
        name = name.upper()

        for i, line in enumerate(lines):
            cols = line.split(",")
            try:
                l_name, f_name = cols[1], cols[2]
            except IndexError:
                print(f"Parser: <{input_file}> is corrupted in line {i+1}.")
                print(f"{"":<7}    Fix it and try again.")
                print("="*50)
                exit(0)

            for field in name.split(" "): # name fields
                # match surname and at least one of the multi first names
                if (l_name in name) and (field in f_name): 
                    filtered_rows.append(cols)
                    output_file += f"_{l_name.lower()}" # add surname to output filename
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
    try:
        with open(output_file, "w") as output_txt:
            output_txt.write(formatted_details)
    except FileNotFoundError:
        print(f"Parser: <{output_file}> is not in the current directory.")
        return
    except PermissionError:
        print(f"Parser: <{output_file}> is open in another process")
        print(f"{"":<7}    or unavailable for the user.")
        return
    
    # read cool_man file contents
    cool_man = "cool_man.txt"
    try:
        content = ""
        with open(cool_man, "r") as text:
            content = text.read()
    except FileNotFoundError:
        print(f"Parser: <{cool_man}> is not in the current directory.")
        print(f"{"":<7}    It will be omitted.")
    except PermissionError:
        print(f"Parser: <{cool_man}> is open in another process")
        print(f"{"":<7}    or unavailable for the user.")
        print(f"{"":<7}    It will be omitted.")

    # append cool_man file contents 
    try:
        with open(output_file, "a") as output_txt:
            output_txt.write(content)
    except FileNotFoundError:
        print(f"Parser: <{output_file}> is not in the current directory.")
    except PermissionError:
        print(f"Parser: <{output_file}> is open in another process")
        print(f"{"":<7}    or unavailable for the user.")
        print(f"{"":<7}    It will be omitted.")


################################################################################


def bonus(input_file:str, output_file:str):
    pattern = re.compile(",S\\w+O,J\\w+O")
    lines = {}

    # read and filter input file content 
    try:
        with open(input_file, "r") as input_txt:
            for i, line in enumerate(input_txt):
                if pattern.search(line):
                    lines[i+1] = line
    except FileNotFoundError:
        print(f"Bonus: <{input_file}> is not in the current directory.")
        return
    except PermissionError:
        print(f"Bonus: <{input_file}> is open in another process")
        print(f"{"":<6}    or unavailable for the user.")
        return
    except KeyboardInterrupt:
        print("Bonus: Exiting program...")
        return
    except Exception:
        print("Bonus: an unexpected error occurred.")
        return

    # update output file contents
    if not lines:
        print(f"Bonus: the pattern was not found in <{input_file}>")
        return

    # append new content
    try:
        with open(output_file, "a") as output_txt:
            output_txt.write("\n\n")
            for i, line in lines.items():
                output_txt.write(f"Found at line {i}: {line}")
    except FileNotFoundError:
        print(f"Bonus: <{output_file}> is not in the current directory.")
    except PermissionError:
        print(f"Bonus: <{output_file}> is open in another process")
        print(f"{"":<6}    or unavailable for the user.")
    except KeyboardInterrupt:
        print("Bonus: Exiting program...")
    except Exception:
        print("Bonus: an unexpected error occurred.")
    else:
        print(f"Bonus: the pattern was found in <{input_file}> line {i}.")


################################################################################


if __name__ == "__main__":
    print("="*50)
    # if you are working as solo, a pair, or a group of three, add your name/s in the list
    # example: names = ['Jose Rizal', 'Taylor Swift', 'Leonardo da Vinci']
    # specify the name of the input file (e.g., BSCPE1-3.csv)

    names = ["eger mirasol"]
    input_file = "BSCPE1-5.csv"
    output_file = parse_data(input_file, names)
    print("Path:", output_file)

    # this is for bonus item only
    bonus(input_file, output_file)
    
    print("="*50)


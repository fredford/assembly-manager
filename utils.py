
def IO_files():

    input_data = []

    input_name = input("Specify input filename: ")
    output_name = input("Specify output filename: ")

    if ".txt" not in input_name:
        input_name = input_name + ".txt"

    if ".txt" not in output_name:
        output_name = output_name + ".txt"

    try:
        input_file = open(input_name,'r+')
        input_lines = input_file.readlines()

        for line in input_lines:
            line = line.rstrip('\n')
            input_data.append(line)

    except:
        input_data = []

    return input_data, open(output_name,'w')



def check_data(input_data):

    if input_data[0] == "Base data generated":
        return True
    else:
        return False
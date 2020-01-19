
from component import Component
from assembly import Assembly
import utils

def main():


    input_data,output_file = utils.IO_files()

    if not utils.check_data(input_data) :
        utils.generate_data(output_file)


    output_file.close()

main()


# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Scourgify              //
# //                                    //
# ////////////////////////////////////////
import sys, csv

# // Main function
def main():
    # // Check provided arguments
    check_arg_validity()
    # // Run the scourgify function
    scourgify()


# // Function to check if the provided args are valid
def check_arg_validity():
    # // Not enough command line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    
    # // Too many command line arguments
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    
    # // Not a valid .csv file
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


# // Function to modify the .csv files
def scourgify():
    try:
        # // Open the input and output files
        input_file = open(sys.argv[1], "r")
        output_file = open(sys.argv[2], "w")
    
    # // If an error occurs, exit the program
    except FileNotFoundError:
        sys.exit("Could not read file")
    
    # // Establish the column data and the column writer
    column_data = csv.DictReader(input_file, delimiter=",")
    column_writer = csv.DictWriter(output_file, ["first", "last", "house"])

    # // Write the CSV header to the output file
    column_writer.writeheader()

    # // Write the CSV input file data to the output file
    # // With it's new format
    for row in column_data:
        last, first = row["name"].split(",")
        column_writer.writerow({
            "first": first.strip(), 
            "last": last, 
            "house": row["house"]
        })

# // Run the main function
if __name__ == "__main__":
    main()
    
# check50 cs50/problems/2022/python/scourgify
# submit50 cs50/problems/2022/python/scourgify
# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Pizza Py               //
# //                                    //
# ////////////////////////////////////////
import sys, csv, tabulate

# // Check if valid command line args
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

# // Check if valid file
if ".csv" not in sys.argv[1]:
    sys.exit("Not a CSV file")

# // Try opening the file, if the file
# // doesn't exist, close the program
try:
    file = open(sys.argv[1], "r")
except FileNotFoundError:
    sys.exit("File does not exist")


# // Establish reader and collect headers
reader = csv.reader(file, delimiter=',')
headers: any = next(reader)

# // Convert the reader in tables
tables: list[any] = [r for r in reader]
# // Create a result string
result: str = tabulate.tabulate(tables, headers, tablefmt="grid")

# // Print the result table
print(result)

# check50 cs50/problems/2022/python/pizza
# submit50 cs50/problems/2022/python/pizza
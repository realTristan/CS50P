# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: Lines of Code          //
# //                                    //
# ////////////////////////////////////////
import sys

# // Check if valid command line args
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

# // Check if valid file
if ".py" not in sys.argv[1]:
    sys.exit("Not a Python file")

# // Try opening the file, if the file
# // doesn't exist, close the program
try:
    file = open(sys.argv[1], "r")
except FileNotFoundError:
    sys.exit("File does not exist")

# // Iterate over the lines and track
# // how many there are
total_lines: int = 0

# // Iterate over the lines
for l in file.read().splitlines():
    # // Check if line is empty
    if len(l.strip()) == 0:
        continue

    # // Check if line starts with a comment
    if not l.strip().startswith("#"):
        total_lines += 1

# // Print the total lines
print(total_lines)

# check50 cs50/problems/2022/python/lines
# submit50 cs50/problems/2022/python/lines
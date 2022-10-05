# ////////////////////////////////////////
# //                                    //
# // Name: Tristan Simpson              //
# //                                    //
# // Assignment: CS50P Shirt            //
# //                                    //
# ////////////////////////////////////////
from PIL import Image, ImageOps
import os, sys

# // Main function
# >> py .\CS50P_Shirt.py before1.jpg after1.jpg
def main():
    # // Check if the command line args are valid
    check_arg_validity()
    # // Check if the files are invalid
    file_check()
    # // Fit the shirt onto the muppet
    fit_shirt()

# // Function to check if the provided args are valid
def check_arg_validity():
    # // Not enough command line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    
    # // Too many command line arguments
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # // Invalid path
    elif not os.path.isfile(sys.argv[1]):
        sys.exit("Invalid input - Path")


# // Check if the files are valid
def file_check():
    formats: list[str] = ["jpg", "jpeg", "png"]
    # // Get the index of the provided file formats.
    # // If an invalid file was provided, then the
    # // variables will be None
    index_1: any = formats.index(sys.argv[1].split(".")[1])
    index_2: any = formats.index(sys.argv[2].split(".")[1])

    # // If one of the files were invalid, exit with invalid
    # // input error message
    if index_1 is None or index_2 is None:
        sys.exit("Invalid input")

    # // Else, return whether the files have the
    # // same format.
    if index_2 != index_1:
        sys.exit("Input and output have different extensions")


# // Fit the shirt onto the muppet
def fit_shirt():
    # // Open the required images and store them
    # // in variables
    shirt = Image.open("shirt.png")
    image = Image.open(sys.argv[1])

    # // Fit the shirt onto the muppet
    image = ImageOps.fit(image, shirt.size)

    # // Paste the shirt onto the image
    image.paste(shirt, shirt)
    # // Then save the image with the name of the 
    # // second provided argument
    image.save(sys.argv[2])


# // Run the main function
if __name__ == "__main__":
    main()

# check50 cs50/problems/2022/python/shirt
# submit50 cs50/problems/2022/python/shirt
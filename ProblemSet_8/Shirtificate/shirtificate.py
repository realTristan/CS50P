from fpdf import FPDF

class PDF(FPDF):

    # // Draw the header of the shirtificate
    def header(self):
        # // Setting image location pox (x/y), width/height,
        self.image("shirtificate.png", 10, 65, 190, 190)

        # // Change the font
        self.set_font("helvetica", "B", 45)

        # // Align the text to the middle of the shirt
        self.text(45, 45, "CS50 Shirtificate")

    # // Draw the footer of the shirtificate
    def footer(self):
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255, 255, 255)
        self.text(70, 140, f"{name} took CS50")


# // Run the program
if __name__ == "__main__":
    # // Get the name of the student
    name = input("What's your name? ")

    # // Create the pdf
    pdf = PDF()
    pdf.add_page()
    pdf.output("shirtificate.pdf")

# check50 cs50/problems/2022/python/shirtificate
# submit50 cs50/problems/2022/python/shirtificate
# Install FPDF via pip: "py -m pip install FPDF"
import fpdf
from fpdf import FPDF

# First all the data we write needs to go to a text file we create that here
text = open("WriteTo.txt", "a")
text.write("This is where all the data will go!")
text.close()

pdf = FPDF() # creates PDF object we can use to edit the PDF with text from the WriteTo.txt

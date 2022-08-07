# Install FPDF via pip: "py -m pip install FPDF"
import fpdf
from fpdf import FPDF

# First all the data we write needs to go to a text file we create that here
text = open("WriteTo.txt", "a")
text.write("This is where all the data will go!")
text.close()

class PDF(FPDF):
  def positionText(self):
    # self.cell()
    # whatever code is needed to ensure text will be placed in the right part of the form

print(text.read())
pdf = PDF()
pdf.positionText()

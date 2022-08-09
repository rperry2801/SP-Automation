# Install FPDF via pip "py -m pip install FPDF"
import fpdf
from fpdf import FPDF

class PDF(FPDF):
  def __init__(self):
    print("Testing PDF Writing Options")
    self.data = input("Write to PDF> ")
    self.writeTextCell(10,10, self.data)
   
  def writeTextCell(self, x, y, user_input):
    self.cell(x, y, user_input, 1)
  def writeUsingWrite(self, loc, user_data):
    self.write(loc, user_data)

pdf = PDF()

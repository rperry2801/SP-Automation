# don't forget to use pip to install the PDF module
# python3 -m pip show PyPDF2 

import PyPDF2
from PyPDF2 import *
from PyPDF2 import PdfFileWriter, PdfFileReader
from pathlib import path

pdf_path = (
  Path.home()
  # enter sharedrive path here
)

# pypdf2
# from PyPDF2 import pdffilereader

# with open("data/Daisy Duck Offer Letter.pdf", "rb") as f:
#     doc = pdffilereader(f)
#     page_1 = doc.getpages(1)
#     print(page_1)

import pdftotext

with open("lorem_ipsum.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

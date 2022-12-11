import camelot

from tabula import read_pdf
# extract all the tables in the PDF file
abc = camelot.read_pdf("C:/Users/HI/Documents/indian%20postal%20system/3507-Article%20Text-6408-1-10-20180104.pdf")
#address of file location

# print the first table as Pandas DataFrame
print(abc[0].df)

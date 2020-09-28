from tabula import read_pdf
import pandas as pd
import time

"""Script to transfor the tables from a pdf file to a csv file without the headers"""


def pdf_to_excel(file):
    dfObj = pd.DataFrame()
    df = read_pdf(file, pages="all", multiple_tables=True)
    for i in df:
        dfObj = dfObj.append(i, ignore_index=True)
    dfObj.to_excel("700_lijn_data.xlsx")



pdf_to_excel("pdf_data.pdf")

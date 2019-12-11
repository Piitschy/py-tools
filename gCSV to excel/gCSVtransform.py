#! python3

import os
from openpyxl import Workbook

def openCSV(name):
    if name[:-4] != ".csv":
        name=name+".csv"
    with open(name,"r") as f:
        lines=f.readlines
    ret=[line.split(';') for line in lines]
    return ret


def writeLine(worksheet,line,content):
    for e,cell in zip(content,[line+str(i) for i in range(len(content)+1)]):
        worksheet[cell] = e



wb = Workbook()
ws1=wb.create_sheet("Contacts")
firstLine=["name","fist name","tel1","tel2","mail","web","facbook","instagram"]
writeLine(ws1,'A',firstLine)
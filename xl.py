import openpyxl as xl
from openpyxl.chart import BarChart, Reference, axis
from graph import process_workbook


filename=input("Enter the filename:")
process_workbook(filename)
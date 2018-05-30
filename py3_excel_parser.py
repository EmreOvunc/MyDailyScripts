#!/usr/bin/python3
# EmreOvunc

from pandas import ExcelFile
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--file', help='select a excel file')
data_parser = parser.add_argument_group('[Data Manipulation]')
data_parser.add_argument('--sheet-name', help='give a sheet name')
data_parser.add_argument('--column', help='give a column name')
args = parser.parse_args()

if args.file != '' or args.file != False:
    try:
        excel = ExcelFile(args.file)
        if args.sheet_name != "" and args.sheet_name != None:
            sheet = excel.parse(args.sheet_name)
            if args.column != "" and args.column != None:
                for data in sheet[args.column]:
                    print(data)
            else:
                print('[-]Please, use --column [COLUMN_NAME] to give a column name!')
        else:
            print('[-]Please, use --sheet-name [SHEET_NAME] to give a sheet name!')
    except:
        print('[-]' + str(args.file) + ' file could not found!')
        exit()
else:
    print('[-]Please, use --file [FILENAME] to select an excel file!')
    exit()

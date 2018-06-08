#!/usr/bin/python3
# EmreOvunc
# info@emreovunc.com

from pandas import ExcelFile
from argparse import ArgumentParser
from os import system, path
from hashlib import md5
from datetime import datetime as dt

parser = ArgumentParser()
parser.add_argument('--file', help='select a excel file')
data_parser = parser.add_argument_group('[Data Manipulation]')
data_parser.add_argument('--sheet-name', help='give a sheet name')
data_parser.add_argument('--column', help='give a column name')
args = parser.parse_args()

curr_time = dt.now().strftime("%H-%M-%S")

if path.isdir(args.sheet_name):
    dirc = args.sheet_name + curr_time
else:
    dirc = args.sheet_name    

viewed = open('who_viewed.txt','r')
viewed_line = viewed.readlines()

clicked = open('who_clicked.txt','r')
clicked_line = clicked.readlines()

system('mkdir ' + dirc)
    
system('touch ' + dirc +'/user_md5s.txt')
usermd5s = open(dirc +"/user_md5s.txt","a")

system('touch ' + dirc +'/statistics.txt')
statistics = open(dirc +"/statistics.txt","a")

system('touch ' + dirc +'/user_clicked.txt')
userclicked = open(dirc +"/user_clicked.txt","a")

system('touch ' + dirc +'/user_viewed.txt')
userviewed = open(dirc +"/user_viewed.txt","a")

clickedarr = []
viewedarr  = []
fixedarr   = []

total_clicked    = 0
total_notclicked = 0
total_viewed     = 0
total_user       = 0
total_noaction   = 0
total_error      = 0

for lines in clicked_line:
    md5sums = lines.strip().split(" ")[3]
    if len(md5sums) == 32:
        clickedarr.append(md5sums)

for lines in viewed_line:
    md5sums = lines.strip().split(" ")[3]
    if len(md5sums) == 32:
        viewedarr.append(md5sums)

if args.file != '' or args.file != False:
    try:
        excel = ExcelFile(args.file)
        if args.sheet_name != "" and args.sheet_name != None:
            sheet = excel.parse(args.sheet_name)
            if args.column != "" and args.column != None:
                for data in sheet[args.column]:
                    try:
                        md5s = md5(data.encode()).hexdigest()
                        usermd5s.write(md5s+'\n')
                        total_user += 1
                    except:
                        total_error += 1
                    flag_click = 0
                    for whoclickedsum in clickedarr:
                        if str(md5s) == str(whoclickedsum):
                            flag_click += 1
                            break
                        else:
                            pass
                    if flag_click == 0:
                        userclicked.write('-\n')
                        total_notclicked += 1
                    else: 
                        userclicked.write('+\n')
                        total_clicked += 1
                    flag_viewed = 0
                    for whoviewedsum in viewedarr:
                        if str(md5s) == str(whoviewedsum):
                            flag_viewed += 1
                            break
                        else:
                            pass
                    if flag_viewed == 0:
                        fixedarr.append('-')
                    else: 
                        fixedarr.append('+')
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

viewed.close()
clicked.close()
usermd5s.close()
userclicked.close()

user_click = open(dirc +"/user_clicked.txt","r")
click_line = user_click.readlines()

for ind in range(0, len(fixedarr)):
        if str(fixedarr[ind]).strip() == "+" and str(click_line[ind]).strip() == "-":
            userviewed.write('+\n')
            total_viewed += 1
        elif str(fixedarr[ind]).strip() == "+" and str(click_line[ind]).strip() == "+":
            userviewed.write('+\n')
            total_viewed += 1
        elif str(fixedarr[ind]).strip() == "-" and str(click_line[ind]).strip() == "+":
            userviewed.write('+\n')
            total_viewed += 1
        else:
            userviewed.write('-\n')
            total_noaction += 1

userviewed.close()
user_click.close()

statistics.write('Total Clicked: ' + str(total_clicked) + '\n')
statistics.write('Total NOT Clicked: ' + str(total_notclicked) + '\n')
statistics.write('Total Viewed: ' + str(total_viewed) + '\n')
statistics.write('Total User: ' + str(total_user) + '\n')
statistics.write('Total No Action: ' + str(total_noaction) + '\n')
statistics.write('Total Error: ' + str(total_error) + '\n')

print('Total Clicked: ', total_clicked)
print('Total NOT Clicked: ', total_notclicked)
print('Total Viewed: ', total_viewed)
print('Total User: ', total_user)
print('Total No Action: ', total_noaction)
print('Total Error: ', total_error)

statistics.close()

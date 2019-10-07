#/usr/bin/python3

giden = open('giden.txt','r')
gline = giden.readlines()

total = open('group_template.csv','r')
tline = total.readlines()

for line in tline:
	tot = line.strip()

	cnt = 0

	for line2 in gline:
		
		if line2.strip().upper() in tot:

			break

		else:

			cnt += 1

			#Total number of duplicates 1465
			if cnt >= 1464:

				print(tot)





file = open('count', 'r')
words = file.readlines()
worders = []
total = 0
flag = 0
for word in words:
    for worder in range(0, len(worders)):
        if worders[worder][0].strip() == word.strip():
            worders[worder] = (worders[worder][0].strip(), int(worders[worder][1]) + 1)
            flag = 1
            break
        else:
            flag = 0
    if flag == 0:
        worders.append((word, 1))

for words in worders:
    print(words[0].strip() + ' | ' + str(words[1]))
    total += int(words[1])

print('\nTotal: ', total)


import csv

file = open('perswitch_perinterface_aggre_stats.csv')

csvreader = csv.reader(file)
header = []
header = next(csvreader)

pagesList = []

idCounter = 0

for row in csvreader:
    if len(pagesList) == 0:
        templist = [idCounter,row[1],int(row[3]) + int(row[4])]
        pagesList.append(templist)
        idCounter += 1
    elif row[1] == pagesList[len(pagesList)-1][1]:
        pagesList[len(pagesList)-1][2] += int(row[3]) + int(row[4])
    else:
        templist = [idCounter,row[1],int(row[3]) + int(row[4])]
        pagesList.append(templist)
        idCounter += 1


file.close()# open the file in the write mode
with open('./temp.csv', 'w', encoding='UTF8') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    for el in pagesList:
        writer.writerow(el)



	    # temp_row = [idCounter,el,pagesDict[el]]
	    # writer.writerow(temp_row)
	    # idCounter += 1
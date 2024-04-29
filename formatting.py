import csv

with open('startups.tsv', 'r') as tsvfile:
    reader = csv.reader(tsvfile)
    data = [row for row in reader]


#using list comprehension to format csv
data = [[cell.replace('\t\t', '\tø\t') for cell in row] for row in data]
clean1 = [[cell.replace('\t', ',') for cell in row] for row in data]
clean2 = [[cell.replace(',,', ',') for cell in row] for row in data]
clean3 = [[cell.replace('ø		ø', 'ø\tø') for cell in row] for row in data]

clean4 = [[cell.replace('\t\t', '\t') for cell in row] for row in data]

with open('startups-formatted.tsv', 'w') as tsvfile:
    writer = csv.writer(tsvfile)
    writer.writerows(clean4)
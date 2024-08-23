import csv

def rateSchool(school):
    school = school.upper()
    count = 0 #no of times in file
    with open("dataSets/crossings.csv", "r") as fin:
        reader = csv.reader(fin, delimiter=",")
        next(reader, None)
        for row in reader:
            if row[7].upper() == school:
                count += 1
    return count

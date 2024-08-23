import csv
def rateSchool(school):
    school = school.upper()
    count = 0 #no of times in file
    with open("dataSets/bus-services.csv", "r") as fin:
        reader = csv.reader(fin, delimiter=",")
        next(reader, None)
        for row in reader:
            if row[7].upper() == school:
                count = count+1         
    return count



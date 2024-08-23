import csv

def rateSchool(school):
    school = school.upper()
    suburb = ""
    numPlaygrounds = 0
    with open("dataSets/schools.csv", "r") as fin:
        reader = csv.reader(fin, delimiter=",")
        next(reader, None) # remove the header from the iterator
        for row in reader:
            if row[0].upper() == school:
                suburb = row[2].upper()
                break

    with open("dataSets/playgrounds.csv", "r") as fin:
        reader = csv.reader(fin, delimiter=",")
        next(reader, None)
        for row in reader:
            if row[3].upper() == suburb: numPlaygrounds += 1

    return numPlaygrounds



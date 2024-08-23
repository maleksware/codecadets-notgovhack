import buses, playgrounds, crossings
import csv
from fuzzywuzzy import fuzz


def similarity_score(candidate, pattern):
    return -fuzz.partial_ratio(candidate, pattern)


def decapitalise(school_name):
    return " ".join([x[0].upper() + x[1:].lower() for x in school_name.split()])


def rateSchool(school_name):
    schools = []

    with open("dataSets/schools.csv", "r") as fin:
        reader = csv.reader(fin, delimiter=",")
        next(reader, None)
        for row in reader:
            schools.append(row[0].upper())

    schools = list(set(schools))

    schools.sort(key=lambda x : similarity_score(x.upper(), school_name.upper()))

    result = []

    for school in schools[:10]:
        crossingsRating = crossings.rateSchool(school)
        busesRating = buses.rateSchool(school)
        playgroundsRating = playgrounds.rateSchool(school)

        result.append(
            [
                decapitalise(school),
                crossingsRating,
                busesRating,
                playgroundsRating,
                crossingsRating + busesRating + playgroundsRating
            ]
        )

    result.sort(key=lambda x : (similarity_score(x[0].upper(), school_name.upper()), -x[4]))
    

    return result 



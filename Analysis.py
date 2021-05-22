
#Interprets and formats results for file comparison
def analyseFileComp(results):
    aver4, high4, match4 = analyseSingleSize(results[0])
    aver5, high5, match5 = analyseSingleSize(results[0])

    #to do
    pass

#Interprets and formats results for paragraph-structured file comparison
def analyseParagraphComp(results):
    #to do
    pass

#Analyses results for a single size comparison(e.g. results for fingerprint size 4)
def analyseSingleSize(query):
    average = 0.0
    highest = 0
    matchedStrings = set()

    for frac, stringTab in query:
        average += frac
        highest = max(highest, frac)

        for string in stringTab:
            matchedStrings.add(string)


    average /= len(query)

    return (average, highest, matchedStrings)
    pass
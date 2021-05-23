import numpy as np

#Interprets and formats results for file comparison
def analyseFileComp(results):
    aver4, high4, match4 = analyseSingleSize(results[0])
    aver5, high5, match5 = analyseSingleSize(results[1])

    analysed4 = (aver4, high4, match4)
    analysed5 = (aver5, high5, match5)

    return (analysed4, analysed5)
    pass

#Interprets and formats results for paragraph-structured file comparison
def analyseParagraphComp(results):
    #Analyse for 4-length fingerprints
    aver4 = []
    high4 = []
    match4 = []

    results4 = results[0]

    for fractions, strings in results4:
        testAverages = []
        testHighs = []
        testStrings = []

        for index, paragraphFrac in enumerate(fractions):
            paragraphStrings = strings[index]

            parAver, parHigh, parStrings = analyseSingleParagraph(paragraphFrac, paragraphStrings)

            testAverages.append(parAver)
            testHighs.append(parHigh)
            testStrings.append(parStrings)

        aver4.append(testAverages)
        high4.append(testHighs)
        match4.append(testStrings)

    aver4 = mergeAverages(aver4)
    high4 = mergeHighs(high4)
    match4 = mergeStrings(match4)
    analysed4 = (aver4, high4, match4)

    #Repeat for 5-length
    aver5 = []
    high5 = []
    match5 = []

    results5 = results[1]

    for fractions, strings in results5:
        testAverages = []
        testHighs = []
        testStrings = []

        for index, paragraphFrac in enumerate(fractions):
            paragraphStrings = strings[index]

            parAver, parHigh, parStrings = analyseSingleParagraph(paragraphFrac, paragraphStrings)

            testAverages.append(parAver)
            testHighs.append(parHigh)
            testStrings.append(parStrings)

        aver5.append(testAverages)
        high5.append(testHighs)
        match5.append(testStrings)

    aver5 = mergeAverages(aver5)
    high5 = mergeHighs(high5)
    match5 = mergeStrings(match5)
    analysed5 = (aver5, high5, match5)

    return (analysed4, analysed5)
    pass

#Analyses results for a single size comparison(e.g. results for fingerprint size 4)
def analyseSingleSize(query):
    average = 0.0
    highest = 0.0
    matchedStrings = set()

    for frac, stringTab in query:
        average += frac
        highest = max(highest, frac)

        for string in stringTab:
            matchedStrings.add(string)


    average /= len(query)

    return (average, highest, matchedStrings)
    pass

#Analyse results for a single paragraph
def analyseSingleParagraph(fractions, strings):
    parAver = 0.0
    parHigh = 0.0
    parStrings = set()

    for frac in fractions:
        parAver += frac
        parHigh = max(parHigh, frac)

    parAver /= len(fractions)

    for stringTab in strings:
        for string in stringTab:
            parStrings.add(string)

    return (parAver, parHigh, parStrings)
    pass

#Merge averages for test results
def mergeAverages(query):
    mergedAver = np.zeros(len(query[0]))


    for fracTab in query:
        mergedAver += fracTab

    mergedAver /= len(query)

    return mergedAver
    pass

#Merge highest values for test results
def mergeHighs(query):
    mergedHigh = np.zeros(len(query[0]))

    for highTab in query:
        mergedHigh = np.maximum(mergedHigh, highTab)

    return mergedHigh
    pass

#Merge matched string sets for test results
def mergeStrings(query):
    mergedString = [set([]) for i in range(len(query[0]))]

    for stringTab in query:
        for index, stringSet in enumerate(stringTab):
            mergedString[index].update(stringSet)

    return mergedString
    pass

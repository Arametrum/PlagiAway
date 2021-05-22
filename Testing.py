import Comparison as cp
import random

ITERATIONS = 5
OFFSET = 7
#All tests for fingerprint sizes 4 and 5

#Tests suspect file with multiple sets of fingerprints
def multFingerprints(suspectFile, comparisonFile):
    results4 = []
    results5 = []

    for i in range(ITERATIONS):
        results4.append(cp.compareFiles(suspectFile, comparisonFile, 4))
        results5.append(cp.compareFiles(suspectFile, comparisonFile, 5))

    return (results4, results5)
    pass

#Tests suspect file with multiple offsets
def offsetFingerprints(suspectFile, comparisonFile):
    results4 = []
    results5 = []

    for i in range(ITERATIONS):
        results4.append(cp.compareFiles(suspectFile[OFFSET * (i + 1):], comparisonFile, 4))
        results5.append(cp.compareFiles(suspectFile[OFFSET * (i + 1):], comparisonFile, 5))

    return (results4, results5)
    pass

#multFingerprints for paragraph-structured files
def multFprintParagraph(suspectFile, comparisonFile):
    results4 = []
    results5 = []

    for i in range(ITERATIONS):
        results4.append(cp.compareParagraphs(suspectFile, comparisonFile, 4))
        results5.append(cp.compareParagraphs(suspectFile, comparisonFile, 5))

    return (results4, results5)
    pass

#offsetFingerprints for paragraph-structured files
def offsetFprintParagraph(suspectFile, comparisonFile):
    results4 = []
    results5 = []

    offsetSuspect = [[par[OFFSET * (i + 1):] for par in suspectFile] for i in range(ITERATIONS)]

    for i in range(ITERATIONS):
        results4.append(cp.compareParagraphs(offsetSuspect[i], comparisonFile, 4))
        results5.append(cp.compareParagraphs(offsetSuspect[i], comparisonFile, 5))

    return (results4, results5)
    pass
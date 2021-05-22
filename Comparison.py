import Fingerprints as fp
import random

#Compare fingerprints and a hand against each other
#Returns fraction of matching fingerprints from suspectFingerprints and list of matched strings
def compareHands(suspectFingerprints, comparisonHand):
    matchingStrings = []

    for rawText, (text, hashVal) in suspectFingerprints:
        if hashVal in comparisonHand[2]:
            if text in comparisonHand[1]:
                matchingStrings.append(rawText)

    fraction = len(matchingStrings)/len(suspectFingerprints)

    return (fraction, matchingStrings)
    pass

#Compare two paragraph-structured documents based on lists of words in each paragraph
def compareParagraphs(suspectDocument, comparisonDocument, fPrintSize):
    suspectParagraphs = len(suspectDocument)
    suspectHandSize = fp.desiredHandSize(suspectParagraphs)

    suspectFingerprints = [fp.generateFingerprints(par, fPrintSize) for par in suspectDocument]
    suspectFingerprints = [fp.prepareFingerprintTable(par, suspectHandSize) for par in suspectFingerprints]

    comparisonParagraphs = len(comparisonDocument)

    comparisonFingerprints = [fp.generateFingerprints(par, fPrintSize) for par in comparisonDocument]
    comparisonHands = [fp.generateParagraphHand(fPrint, comparisonParagraphs) for fPrint in comparisonFingerprints]

    resultFractions = []
    matchingStrings = []

    for fPrint in suspectFingerprints:
        tmpFrac = []
        tmpString = []

        for hand in comparisonHands:
            frac, strng = compareHands(fPrint, hand)

            tmpFrac.append(frac)
            tmpString.append(strng)

        resultFractions.append(tmpFrac)
        matchingStrings.append(tmpString)

    return (resultFractions, matchingStrings)
    pass

#Compare two non-paragraph files
def compareFiles(suspectFile, comparisonFile, fPrintSize):

    pass

#Compare fingerprints and a hand against each other, returns fraction of matching fingerprints from suspectFingerprints and list of matched strings
def compareHands(suspectFingerprints, comparisonHand):
    matchingStrings = []

    for rawText, (text, hashVal) in suspectFingerprints:
        if hashVal in comparisonHand[2]:
            if text in comparisonHand[1]:
                matchingStrings.append(rawText)

    fraction = len(matchingStrings)/len(suspectFingerprints)

    return (fraction, matchingStrings)
    pass

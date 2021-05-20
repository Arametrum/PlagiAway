import random

HAND_SIZE = 200
MIN_HAND_SIZE = 30

#Hash given query string
def rollingHash(query):
    HASH_BASE = 256
    PRIMER = 101

    hashVal = 0
   
    for char in query:
        hashVal = ((hashVal * HASH_BASE) % PRIMER + ord(char)) % PRIMER

    return hashVal
    pass

#Generate fingerprint
def fingerprint(query):
    return (query, rollingHash(query))

#Generate fingerprints of (fPrinSize) size from given table
def generateFingerprints(queryTable, fPrintSize):
    tmp = "a"
    rawTmp = "a"

    fingerprints = []

    for index, word in enumerate(queryTable):
        if index % fPrintSize == 0:
            fingerprints.append((rawTmp, fingerprint(tmp.lower())))

            tmp = ""
            rawTmp = ""

        tmp += word
        rawTmp += word + " "

    fingerprints.pop(0)
    return fingerprints
    pass

#Generate hand based on randomly picked fingerprints
def generateRandomHand(queryTable):
    random.shuffle(queryTable)

    rawText = [rT[0] for rT in queryTable[:HAND_SIZE]]
    text = [T[1][0] for T in queryTable[:HAND_SIZE]]
    hashes = {H[1][1] for H in queryTable[:HAND_SIZE]}

    return (rawText, text, hashes)
    pass

#Generate hand for a paragraph
def generateParagraphHand(queryTable, paragraphNum):
    random.shuffle(queryTable)

    actualSize = max(int(HAND_SIZE/paragraphNum), MIN_HAND_SIZE)

    rawText = [rT[0] for rT in queryTable[:actualSize]]
    text = [T[1][0] for T in queryTable[:actualSize]]
    hashes = {H[1][1] for H in queryTable[:actualSize]}

    return (rawText, text, hashes)
    pass


#Generate hand based on paragraphs
#Generate hand based on a cross pattern
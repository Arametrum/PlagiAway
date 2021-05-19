
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
    fingerprints = []

    for index, word in enumerate(queryTable):
        if index % fPrintSize == 0:
            fingerprints.append(fingerprint(tmp.lower()))
            tmp = ""

        tmp += word

    return fingerprints
    pass

#Generate hands based on randomly picked fingerprints
def generateRandomHands(queryTable):
    
    pass

#Generate hands based on paragraphs
def generataParagraphHands(paragraphTable):

    pass

#Generate hands based on a cross pattern
def generateCrossHands(queryTable):

    pass

#Generate hands based on most common fingerprints
def generateCommonHands(queryTable):

    pass
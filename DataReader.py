
#Split line into words
def prepLine(queryLine):
    tokens = queryLine.split()
    parsedTokens = []

    for token in tokens:
        parsedTokens.append(token.strip(""" ,.:;?/!"()"""))

    return parsedTokens
    pass

#Read entire file and split into words; on fail return []
def readFile(path):
    data = []

    try:
        with open(path, 'r', encoding = 'UTF-8') as file:

            for line in file:
                words = prepLine(line.lower())
            
                for i in words:
                    data.append(i)
    except:
        return []

    return data
    pass

#Read file and split into paragraphs
def readByParagraphs(path):
    data = []

    try:
        with open(path, 'r', encoding = 'UTF-8') as file:
            paragraph = []

            for line in file:
                words = prepLine(line.lower())
            
                if line == "\n":
                    data.append(paragraph)
                    paragraph = []

                for i in words:
                    paragraph.append(i)

            if paragraph:
                data.append(paragraph)
    except:
        return []

    return data
    pass
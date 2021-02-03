listOfLists = []
listOfLists.append([''])  # listOfLists[0] = the empty string


with open('words.txt') as inputFile:
    words = inputFile.readlines()

for word in words:
    if(len(word) > len(listOfLists)):
        for i in range(len(listOfLists), len(word)):
            listOfLists.append([])

    # Remove the '\n' from each word
    word = "'" + word[0: len(word)-1] + "'"

    # Put each word into the list corresponing to its length.
    listOfLists[len(word) - 2].append(word)

inputFile.close()

with open('sortedWords.txt', 'w') as outputFile:
    outputFile.write('export const listOfLists = [')

    # Copy lists in order of increasing size.
    for wordList in listOfLists:
        numberOfWords = len(wordList)
        if numberOfWords == 0:
            outputFile.write('[],\n')
            continue
        outputFile.write('[')
        for i in range(0, numberOfWords):
            outputFile.write(wordList[i])
            if i < numberOfWords - 1:
                outputFile.write(', ')
            else:
                outputFile.write('],\n')

    outputFile.write(']')
    outputFile.close()

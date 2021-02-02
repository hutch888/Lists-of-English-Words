# Lists-of-English-Words
Lists of English words sorted alphabetically and by length

words.txt is an alphabetically arranged list of words from [dwyl/english-words](https://github.com/dwyl/english-words).
  sortedWords.txt contains a list of lists called listOfLists. Each inner list contains the words from words.txt of a given length. For example, listOfLists[3] contains the words of length 3. If there are no words whose length corresponds to the index of a given list, then that list is empty. For example there a no words that are 30 characters long so listOfLists[30] = [].
  wordSorter.py is the Python 3 script used to create sortedWords.txt from words.txt.

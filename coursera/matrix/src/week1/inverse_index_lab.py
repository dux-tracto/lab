# version code d345910f07ae
from random import randint
coursera = 1
def printTaskMarker(taskNum): print("\n**** task: " + str(taskNum) + " ****")	
# Please fill out this stencil and submit using the provided submission script.





## 1: (Task 1) Movie Review
## Task 1
printTaskMarker(1)
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    reviewSummary = [ "feel good hit", "not Scottish therefore crap", "OK", "not good", ]
    return reviewSummary[randint(0,len(reviewSummary) - 1)]
print("movie_review: " + movie_review("Pulp Fiction"))


## 2: (Task 2) Make Inverse Index
printTaskMarker(2)
searchIndex = dict();
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.
    Distinguish between an occurence of a string (e.g. "use") in the document as a word
    (surrounded by spaces), and an occurence of the string as a substring of a word (e.g. "because").
    Only the former should be represented in the inverse index.
    Feel free to use a loop instead of a comprehension.

    Example:
    >>> makeInverseIndex(['hello world','hello','hello cat','hellolot of cats']) == {'hello': {0, 1, 2}, 'cat': {2}, 'of': {3}, 'world': {0}, 'cats': {3}, 'hellolot': {3}}
    True
    """
    lineNumber = 0;
    try:
        theData = open(strlist)
        for line in theData:
            wordList = line.split()
            for word in wordList:
                if word in searchIndex:
                    s = searchIndex.get(word)
                else:
                    s = set()
                s.add(lineNumber)
                searchIndex[word] = s
            lineNumber += 1
        theData.close()
    except FileNotFoundError:
        print("File not found. Search index will be empty and boring!")
    except ZeroDivisionError:
        print("Divide by 0")

makeInverseIndex("stories_small.txt")
print(searchIndex)


## 3: (Task 3) Or Search
printTaskMarker(3)
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    Feel free to use a loop instead of a comprehension.
    
    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> orSearch(idx, ['Bach','the'])
    {0, 2, 3, 4, 5}
    >>> orSearch(idx, ['Johann', 'Carl'])
    {0, 2, 3, 4, 5}
    """
    resultSet = None
    for word in query:
        if word in inverseIndex:
            if resultSet == None:
                resultSet = inverseIndex[word]
            else:
                resultSet = resultSet.union(inverseIndex[word])
    return resultSet

q = "fighting pilot"
resultSet = orSearch(searchIndex, q.split())
print("orSearch(" + q + ") results: " + str(resultSet))

##4: (Task 4) And Search
printTaskMarker(4)
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    Feel free to use a loop instead of a comprehension.

    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> andSearch(idx, ['Johann', 'the'])
    {2, 3}
    >>> andSearch(idx, ['Johann', 'Bach'])
    {0, 4}
    """
    resultSet = None
    for word in query:
        if word in inverseIndex:
            if resultSet == None:
                resultSet = inverseIndex[word]
            else:
                resultSet = resultSet.intersection(inverseIndex[word])
    if len(resultSet) == 0:
        return None
    else:
        return resultSet


q = "fighting pilot"
q = "Today he draw"
resultSet = andSearch(searchIndex, q.split())
print("andSearch(" + q + ") results: " + str(resultSet))
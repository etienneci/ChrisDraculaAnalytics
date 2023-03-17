# This function returns the entirety of "Dracula" as a string
def readBook():
  f = open("dracula.txt", "r")
  s = f.read().replace("-", " ")
  f.close()
  return ''.join(c for c in s if c.isalnum() or c == " ")

print(" ====#=# Results #=#====")
print()
# read the text of dracula
draculaText = readBook()

# seperate each word for parsing
words = draculaText.lower()
words = words.split()

# find the word that appears the most
# create empty dictionary to hold words and amount of appearances
wordCounts = {
  
}

for word in words:
  if word in wordCounts:
    wordCounts[word] += 1
  else:
    wordCounts[word] = 1
# check and store which word appears most. display result
mostCommon = ""
commonCount = 0
for word, count in wordCounts.items():
  if count > commonCount:
    mostCommon = word
    commonCount = count
print(f"'{mostCommon}' is the word that appears the most, it appears {commonCount} times.")
print()

# find unique 4 letter words
# create empty dictionary for unique words
uniqueWords = {
  
}

# go through words and check if it is 4 letters. store if it has not been stored yet
numberOfUnique = 0
for word in words:
  if len(word) == 4:
    if word not in uniqueWords:
      uniqueWords[word] = 1
      numberOfUnique += 1
    else:
        uniqueWords[word] = +1
print(f"There are {numberOfUnique} unique 4 letter words.")
print()

# find words that show up more than 500 times
# loop through each word, if it shows up more than 500 times, print it and the amount of times
print("I noticed these words show up more than 500 times.")
print()

for word, count in wordCounts.items():
  if count > 500:
    print(f"{word} - {count} ")

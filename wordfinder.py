"""Word Finder: finds random words from a dictionary."""

import random
class WordFinder:
    
    def __init__(self, file):
        self.words = []
        with open(file) as file:
            for line in file:
                tempWord = line
                tempWord = tempWord[0:-2]
                self.words.append(tempWord)
    
    def random(self):
        temp = random.randint(0,len(self.words))
        return(self.words[temp])
    
class SpecialWordFinder:
    
    def __init__(self, file):
        self.words = []
        with open(file) as file:
            for line in file:
                if line == "" or line[0:1] == "#":
                    pass
                else:
                    tempWord = line
                    tempWord = tempWord[0:-2]
                    self.words.append(tempWord)
    
    def random(self):
        temp = random.randint(0,len(self.words))
        return(self.words[temp])
    

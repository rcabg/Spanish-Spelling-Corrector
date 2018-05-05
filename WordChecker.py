# -*- coding: utf-8 -*-
"""
Created on Sat May  5 13:32:08 2018

@author: rcabg
"""

import WordEdition as we

class WordChecker:
    def __init__(self, dictionary, totalFreq):
        self.dictionary    = dictionary
        self.wordEdition   = we.WordEdition()
        self.totalFreq     = totalFreq
        self.maxCandidates = 3
        
    def knownWords(self, words):
        return list(word for word in words if word in self.dictionary)
    
    def candidates(self, word):
        return (self.knownWords([word]) or
                self.knownWords(self.wordEdition.allEdits(word)) or
                self.knownWords(self.wordEdition.allEdits2(word)) or
                [word])
    
    def getWordProbability(self, word):
        return self.dictionary[word] / self.totalFreq

    def getCorrection(self, word):
        print("You wrote: " + word)
        
        candidates = self.candidates(word)
        if len(candidates) == 0:
            print("**NO CANDIDATES**")
        elif candidates[0] == word:
            print("**NO CANDIDATES**")
        else:
            print("Probably you mean to say: ")
            count = 0
            for candidate in candidates:
                print(" - " + candidate)
                count += 1
                if count == self.maxCandidates:
                    break

    def setMaxCandidates(self, maxCandidates):
        self.maxCandidates = maxCandidates
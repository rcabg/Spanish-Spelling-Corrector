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
        self.maxCandidates = 5
        
    def knownWords(self, words):
        return list(word for word in words if word in self.dictionary)
    
    def candidates(self, word):
        candidates = (self.knownWords([word]) or
                      self.knownWords(self.wordEdition.allEdits(word)) or
                      self.knownWords(self.wordEdition.allEdits2(word)))
        return self.sortCandidates(set(candidates))
        
    def sortCandidates(self, candidates):
        #numCandidates = len(candidates)
        totalFreq = 0
        wordList = list()
        freqList = list()
        for candidate in candidates:
            freq = self.dictionary[candidate]
            totalFreq += freq
            if len(freqList) == 0:
                wordList.append(candidate)
                freqList.append(freq)
            else:
                for index, val in enumerate(freqList):
                    if freq > val:
                        freqList.insert(index, freq)
                        wordList.insert(index, candidate)
                        break
                    
                    if index + 1 == len(freqList):
                        freqList.append(freq)
                        wordList.append(candidate)
                        break
         
        for index, val in enumerate(freqList):
            freqList[index] = freqList[index] * 100 / totalFreq 
            
        return (wordList, freqList)
    
    def getWordProbability(self, word):
        return self.dictionary[word] / self.totalFreq

    def getCorrection(self, word):
        print("You wrote: " + word)
        
        words, freqs = self.candidates(word)
    
        if len(words) == 0:
            print("**NO CANDIDATES**")
        elif words[0] == word:
            print("**Word is correct**")
        else:
            print("Probably you mean to say: ")
            count = 0
            for index, candidate in enumerate(words):
                print(" *- " + candidate + " - " + str('%.2f' % freqs[index]) + " %")
                count += 1
                if count == self.maxCandidates:
                    break

    def setMaxCandidates(self, maxCandidates):
        self.maxCandidates = maxCandidates
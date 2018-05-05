# -*- coding: utf-8 -*-
"""
Created on Tue May  1 16:49:41 2018

@author: rcabg
"""

import SpanishWordFreq as swf
import WordChecker     as wc

filePath = "5000_frecuencias.txt"
spanishWords = swf.SpanishWordsFreq(filePath)

wordChecker = wc.WordChecker(spanishWords.words, spanishWords.totalFreq)

print("Spanish Spelling Checker")
print("Please write 'q' or 'quitprogram' in order to exit")

while(1):
    word = input("Write a Spanish word to be checked: ")
    if word == "quitprogram" or word == 'q':
        print("Exit...")
        break
    
    wordChecker.getCorrection(word)
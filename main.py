# -*- coding: utf-8 -*-
"""
Created on Tue May  1 16:49:41 2018

@author: rcabg
"""

import sys
from spanish_word_freq import SpanishWordFreq
from word_chekcer import WordChecker

def main(argv):
    if len(argv) == 0:
        filePath = "10000_frecuencias.txt"
    else:
        filePath = argv[1]

    spanishWords = SpanishWordFreq(filePath)
    
    wordChecker = WordChecker(spanishWords.words, spanishWords.totalFreq)
    
    print("Spanish Spelling Checker")
    print("Please write 'q' or 'quitprogram' in order to exit")
    
    while(1):
        word = input("Write a Spanish word to be checked: ")
        if word == "quitprogram" or word == 'q':
            print("Exit...")
            break
        
        wordChecker.getCorrection(word.lower())

if __name__ == "__main__":
    main(sys.argv[1:])
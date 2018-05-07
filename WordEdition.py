# -*- coding: utf-8 -*-
"""
Created on Fri May  4 23:49:58 2018

@author: rcabg
"""

class WordEdition:
    def __init__(self):
        self.letters = 'abcdefghijklmnopqrstuvwxyzáéíóúüñ'
        self.vowels  = 'aeiouáéíóúü' ### TODO: check spanish typical vowel mistakes
        self.qwerty  = {'q':'aws',
                        'w':'qase',
                        'e':'wsdr',
                        'r':'edft',
                        't':'rfgy',
                        'y':'tghu',
                        'u':'yhji',
                        'i':'ujko',
                        'o':'iklp',
                        'p':'olñ',
                        'a':'qzws',
                        's':'azxwde',
                        'd':'esxcfr',
                        'f':'rdcvgt',
                        'g':'tfvbhy',
                        'h':'gbnjuy',
                        'j':'uhnmki',
                        'k':'ijmlo',
                        'l':'opkñ',
                        'ñ':'opl',
                        'z':'asx',
                        'x':'zsdc',
                        'c':'xdfv',
                        'v':'cfgb',
                        'b':'vghn',
                        'n':'bhjm',
                        'm':'njk',
                        'á':'qzws',
                        'é':'wsdr',
                        'í':'ujko',
                        'ó':'iklp',
                        'ú':'yhji',
                        'ü':'yhji'}
        
        lowerQwerty = dict(self.qwerty)
        for lowerKey in lowerQwerty.keys():
            self.qwerty[lowerKey.upper()] = lowerQwerty[lowerKey].upper()

    def splits(self, word):
        return [(word[:i], word[i:]) for i in range(len(word) + 1)]
    
    def deletes(self, word):
        return [left + right[1:] for left, right in self.splits(word) 
                if right]
    
    def transposes(self, word):
        return [left + right[1] + right[0] + right[2:] for left, right in 
                self.splits(word) if len(right) > 1]
    
    def replaces(self, word):
        return [left + letter + right[1:] for left, right in self.splits(word)
                if right for letter in self.letters]
    
    def inserts(self, word):
        return [left + letter + right for left, right in self.splits(word) 
                for letter in self.letters]
    
    def qwertyTypos(self, word):
        qwerty = []
        for left, right in self.splits(word):
            if right:
                for letter in self.qwerty[right[0]]:
                    qwerty.append(left + letter + right[1:])
        return qwerty
        
    def allEdits(self, word):
        return set(self.deletes(word) +
                   self.transposes(word) + 
                   self.replaces(word) + 
                   self.inserts(word) +
                   self.qwertyTypos(word))
    
    def allEdits2(self, word):
        return (edits2 for edits1 in self.allEdits(word) for edits2 
                in self.allEdits(edits1))

# SpanishSpellingCorrector

A Spanish spelling corrector for Python 3 that tries to propouse a corrected form of a Spanish introduced word. Spanish most frequent words text file must be downloaded from Real Academia Española website: [link](http://corpus.rae.es/lfrecuencias.html) (*10000 most frequent words file is recommended*) 

This project has been created for the second deliverable of Natural Language Processing (PLN) from MULCIA, University of Seville (Procesamiento del Lenguaje Natural, Máster Universitario en Lógica, Computación e Inteligencia Artificial, Universidad de Sevilla, 2017/2018)  

## Instructions

 1. Clone the repository
 2. Download the 10000 most frequent words file from  [here](http://corpus.rae.es/lfrecuencias.html) and place it in the repository folder
 3. Run main.py [arg1] where arg1 is the path to the words file downloaded beforehand.
 4. Follow the terminal instructions

## Examples
```
Spanish Spelling Checker
Please write 'q' or 'quitprogram' in order to exit

Write a Spanish word to be checked: mieercoles
You wrote: mieercoles
Probably you mean to say: 
 *- miércoles - 100.00 %

Write a Spanish word to be checked: chaqeta
You wrote: chaqeta
Probably you mean to say: 
 *- chaqueta - 100.00 %

Write a Spanish word to be checked: camio
You wrote: camio
Probably you mean to say: 
 *- cambio - 42.76 %
 *- campo - 28.11 %
 *- camino - 27.25 %
 *- camilo - 1.89 %

Write a Spanish word to be checked: fueza
You wrote: fueza
Probably you mean to say: 
 *- fuera - 62.72 %
 *- fuerza - 37.28 %
 ```


#!/usr/bin/python
# -*- coding: cp1252 -*-
import random
class Cipher:
    
    def __init__(self):
        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","é","à","ç","è","ê","â","ë","ä"," ","?",";",".",":","!","\"","'","0","1","2","3","4","5","6","7","8","9"]
        self.alphabetTransition = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","é","à","ç","è","ê","â","ë","ä"," ","?",";",".",":","!","\"","'","0","1","2","3","4","5","6","7","8","9"]
        self.alphabetCipher = [""]*78
        self.cipherText=""
    def cipher(self, text_):
        textCrypt = ""
       
        
        self.generateAlphabet()
        text_temp  =[]
        for e in text_:
            cc = self.alphabet.index(e)
            text_temp.append(self.alphabetCipher[cc])

        textCrypt="".join(text_temp)
        self.cipherText = textCrypt
        print "your cipher text : "+self.cipherText

    def generateAlphabet(self):
        i=0
        while i < 78:
            y = random.randint(0,len(self.alphabetTransition)-1)
            self.alphabetCipher[i] = self.alphabetTransition[y]
            del self.alphabetTransition[y]
            
            i = i +1

    def uncipherText(self):
        
        if self.cipherText != "":
            textDecryp =""
            text_temp = []
            for e in self.cipherText:
                cc = self.alphabetCipher.index(e)
                text_temp.append(self.alphabet[cc])
            textDecrypt = "".join(text_temp)
            print "Your text is : "+textDecrypt
            

        else:
            print "Sorry but, the following ressource is missing : textCipher"









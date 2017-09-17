from cipher import *
print "Welcome to the text cipher !"

textInput = raw_input("Enter your text here:")

test = Cipher()
test.cipher(textInput)

test.uncipherText()

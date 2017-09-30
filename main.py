from cipher import *

print "Welcome to the text cipher !"

print "01 - For cipher your text"
print "02 - For uncipher your cipher text (your text must be already cipher)"
print "03 - For quit the software"
choiceUser = False
alreadyCipher = False
while(choiceUser  == False):

    choiceInput = raw_input(">")

    if(choiceInput == "01" or choiceInput == "1"):
        cipher = Cipher()
        textInput = raw_input("Enter your text here:")
        passwordInput = raw_input("Now, enter your password here :")
        cipher.cipher(passwordInput, textInput)
        alreadyCipher = True

    elif(choiceInput == "02" or choiceInput == "2"):
        cipher = Cipher()
        textInput = raw_input("Enter the url of your file text here :")
        passwordInput = raw_input("Now, enter your password here :")
        cipher.uncipherText(passwordInput, textInput)

    elif(choiceInput  == "03" or choiceInput == "3"):
        choiceUser = True
        print "See you soon !"

    else:
        print "Wrong choice, let's try again  !"

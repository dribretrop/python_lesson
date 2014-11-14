def loop(): 
    pyg = 'ay'
       
    original = raw_input("*** Type EXIT to exit ***\n Enter a word:")
    
    
    if original == "exit" or original == "EXIT" or original =="Exit":
            print "Bye"
    elif len(original) > 0 and original.isalpha():  
            word = original.lower()
            first = word[0] #select first letter
            new_word = word + first + pyg  #concat letter
            new_word = new_word[1:len(new_word)]#remove 1st letter and follow len
            print new_word
            loop()
    else:
            print 'empty or have number or white space'
            loop()
        
loop()
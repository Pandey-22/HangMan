import random 
def hangman():
    list_of_words=['eduyear','hangman','india','laptop']
    word=random.choice(list_of_words)
    turns=10
    guessmade=''
    vailed_entry=set('aabcdefghijklmnopqrstuvwxyz')
    while len(word)>0:
        Main_word=" "
        for letter in guessmade:
            if letter in guessmade:
                Main_word=Main_word+letter
            else:
                Main_word=Main_word+"_ "
        if Main_word==word:
            print(Main_word)
            print("You won!!")
            break
        print("guess the word",Main_word)
        guess=input()
        if guess in vailed_entry:
            guessmade=guessmade+guess
        else:
            print("enter vaild character")
            guess=input()
        if guess not in word:
            turns=turns-1
            if turns==9:
                print("9 turns left!!")
                print("---------------")
            if turns==8:
                print("8 turns left!!")
                print("--------------")
                print("   o          ")
            if turns==7:
                print("7 turns left!!")
                print("--------------")
                print("   o          ")
                print("   |          ")
            if turns==6:
                print("6 turns left!!")
                print("--------------")
                print("   o          ")
                print("   |          ")
                print("   /          ")
            if turns==5:
                print("5 turns left!!")
                print("--------------")
                print("   o          ")
                print("   |          ")
                print("  / \         ")
            if turns==4:
                print("4 turns left!!")
                print("--------------")
                print("   \o         ")
                print("    |         ")
                print("   / \        ")
            if turns==3:
                print("3 turns left!!")
                print("--------------")
                print("   \o/        ")
                print("    |         ")
                print("   / \        ")
            if turns==2:
                print("2 turns left!!")
                print("--------------")
                print("   \o/  |     ")
                print("    |         ")
                print("   / \        ")
            if turns==1:
                print("only 1 turn left!!!hangman on this last breath")
                print("1 turns left!!")
                print("--------------")
                print("   \o/_|      ")
                print("    |         ")
                print("   / \        ")
            if turns==0:
                print("you loose")
                print("you let a good man die")
                print("only 1 turn left!!!hangman on this last breath")
                print(" turns left!!")
                print("--------------")
                print("     o_|      ")
                print("    /|\       ")
                print("    / \       ")
            if turns==0:
                print("you loose")
            print("you let a good man die")
            # break
name=input("enter your name")
print("WELCOME",name,"!")
print("----------------------------")
print("Try to guess the word in less than 0 attempts")
hangman()
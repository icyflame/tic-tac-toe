from Tkinter import *

flag = True

##def play():
##
##    t = Tk()
##
##    root = Frame(t)
##
##    root.grid()
##
##    global p
##
##    p = {}
##
##    for i in range(9):
##
##        p[(i/3, i%3)] = Button(root, text=' ', command=toggle(i/3, i%3))
##
##        p[(i/3, i%3)].grid(row=i/3, column=i%3)
##
##    mainloop()
##
##def toggle(a, b):
##
##    def toggle1():
##
##        global flag
##
##        print "Flag is: ", flag
##
##        try:
##
##            if flag:
##                
##                p[a, b].config(text="X")
##
##            else:
##
##                p[a, b].config(text="O")
##
##            flag = not flag
##            
##        except:
##
##            raise IOError
##        
##    return toggle1

##def drawBoard(X, O):
##
##    t = Tk()
##
##    root = Frame(t)
##
##    root.pack()
##
##    for i in range(9):
##
##        if (i/3 + 1, i%3 + 1) in X.filled:
##
##            Label(root, text='X').pack()
##
##        elif (i/3 + 1, i%3 + 1) in O.filled:
##
##            Label(root, text='O').pack()
##
##
##        else:
##
##            Label(root, text='None').pack()
##
####
####    for i in range(9):
####
####        Label(root, text='done').pack()
##
##    Button(root, command=t.destroy).pack(side='top')
##
##    mainloop()
##
##    return None
##

entered = []

class Player:

    def __init__(self, playwith):

        self.icon = playwith #X or O

        self.filled = [] #the coords that this player has filled


        self.play()

    
    def toggle(self, a, b):

        def toggle1():

            global flag

            print "Flag is: ", flag

            try:

                if flag:
                    
                    p[a, b].config(text="X")

                else:

                    p[a, b].config(text="O")

                flag = not flag


                self.fillOne(a, b)
                
            except:

                raise IOError
            
        return toggle1

    def play(self):

        t = Tk()

        root = Frame(t)

        root.grid()

        global p

        p = {}

        for i in range(9):

            p[(i/3, i%3)] = Button(root, text=' ', command=self.toggle(i/3, i%3))

            p[(i/3, i%3)].grid(row=i/3, column=i%3)

        mainloop()

    def fillOne(self, x = None, y = None):

        done = True
        
        while(done):

            print
            print "player ",self.icon

            if(x == None and y == None):

                x = input("Enter the x coord of your entry:")
                y = input("Enter the y coord of your entry:")

            a = (x, y)

            if not a in entered:

                entered.append(a)
                done = False
                self.filled.append(a)

                won = self.checkWon()


                if(won):

                    return True


                else:

                    return False


            else:

                alert("You have already entered")


    def checkWon(self):

##        will check if this player has won the game
##
##
##        conditions for winning:
##
##
##            1. any three x are the same
##            2. any three y are the same
##            3. any three points form a diagonal

        #case 1 and 2
        
        x = []
        y = []

        freq1 = {}
        freq2 = {}
        
        for i in self.filled:

            x.append(i[0])
            y.append(i[1])

        for i in x:

            try:

                freq1[i] += 1

            except:

                freq1[i] = 1

        for i in y:

            try:

                freq2[i] += 1

            except:

                freq2[i] = 1


        for i in freq1:

            if freq1[i] >= 3:

                return True
            
        for i in freq2:

            if freq2[i] >= 3:

                return True


        #case 3

        f = 0

        for i in range(1, 4):

            if(i, i) in self.filled:

                f += 1


        if f == 3:

            return True     
        
        return False



def startPlay():


    X = Player('X')

    O = Player('O')


    won = False

    while(not won):

        won = X.fillOne()

        if(not won):
            
            won = O.fillOne()

            if(won):

                print "Player O won the game"

        else:

            print
            print
            print "Player X won the game"


        drawBoard(X, O)

        print X.filled
        print O.filled


    print X.filled
    print O.filled

#startPlay()
#play()

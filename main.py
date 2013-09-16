class Player(object):

    def __init__(self, name, icon):

        self.name = name

        self.icon = icon

        self.filled = []

        self.board = Board()        

    def play(self):

        pass

    def hasWon(self):

        pass


def Board(object):

    def __init__(self):

        p = {}

        t = Tk()

        root = Frame(t)

        root.grid()

        global p

        p = {}

        for i in range(9):

            p[(i/3, i%3)] = Button(root, text=' ', command=self.toggle(i/3, i%3))

            p[(i/3, i%3)].grid(row=i/3, column=i%3)

        mainloop()

    def toggle(self):

        def toggle1():

            p[(a, b)].config(text=self.player.icon)

from blessed import Terminal
t = Terminal()
class Symbol:
    def __init__(self):
        self.heart =  u"\u2665"
        self.larrow = u"\u2190"
        self.rarrow = u"\u2B95"
        self.darrow = u"\u2193"
        self.uarrow = u"\u2191"
s = Symbol()
class Menu:
    def __init__(self):
        from blessed import Terminal
        t = Terminal()
        self.cursor_color = t.color(196)
        self.cursor_str = s.rarrow
        self.cursorPosition = 1
    def refreshCursor(self):
        self.cursorPosition = 1
    def cls(self):
        import os
        os.system("clear")
    def vert(self, title, *content):
        with t.hidden_cursor():
            while True:
                self.cls() #clears the screen
                self.iteration = 0 #this attribute holds the choice # in the menu
                print(title) #prints out the menu title
                for msg in content:
                    self.iteration += 1 #increments to the next iteration
                    if self.iteration == self.cursorPosition: #check if the cursor position matches the choice #
                        print("{} {}".format(self.cursor_color(self.cursor_str), self.cursor_color(msg)))#prints out the choice, with a marker
                    else:
                        print("{} {}".format(" "*len(self.cursor_str), msg)) #prints a plain choice
                with t.cbreak(): #wait for keyboard input
                    k = t.inkey(timeout=None) #read for keypresses
                    if k.name == "KEY_UP":
                        if self.cursorPosition > 1:
                            self.cursorPosition -= 1
                        elif self.cursorPosition <= 1:
                            self.cursorPosition = len(content)
                        continue
                    elif k.name == "KEY_DOWN":
                        if self.cursorPosition < len(content):
                            self.cursorPosition +=1
                        elif self.cursorPosition >= len(content):
                            self.cursorPosition = 1
                        continue
                    elif k.name == "KEY_ENTER" or k == "z":
                        return self.cursorPosition
m = Menu()
x = m.vert("You are defusing a bomb. Cut a wire","Red wire","Blue wire")
if x == 1:
    print("You successfully defused the bomb.")
elif x == 2:
    print("You failed. BOOM!")
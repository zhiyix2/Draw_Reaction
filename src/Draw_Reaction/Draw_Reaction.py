

"""
Author: Zhiying Xie
"""


from tkinter import Tk, Canvas, Frame, BOTH
import Read_Compound_Reaction

class Draw_Reaction(Frame):

    def __init__(self):
        super().__init__()
        reaction_list = Read_Compound_Reaction.get_reaction_list(Read_Compound_Reaction.readFile("Result2.txt"))

        inputList = Read_Compound_Reaction.get_reaction_data(reaction_list)
        inputList = Read_Compound_Reaction.get_compound_reaction(inputList)

        print(inputList)
        
        self.initUI(inputList)

    # Draw the Canvas, boxes and texts
    # InputList a List Object of Compound Reaction Lists
    def initUI(self, inputList):

        self.master.title("Draw Reaction")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        margin = 10
        height = 40
        width = 100
        rows = len(inputList)
        column = len(inputList[1])
        windowHeight = (rows * margin + 1) + (height * rows + 1)
        windowWidth = (rows * margin + 1) + (column * width + 1)
        ##height_width = "{}x{}+300+300".format(windowWidth, windowHeight)
        count = 0
        for i in range(1, rows + 1, 1):
            print(len(inputList[i-1]))
            reactant = True
            for j in range(1, len(inputList[i - 1]) + 1, 1):
                x0 = margin * j + (j - 1) * width
                y0 = margin * i + (i - 1) * height
                x1 = margin * j + width * j
                y1 = margin * i + height * i
                #print("x0 = {} y0 = {} x1 = {} y1 = {}".format(x0, y0, x1, y1))
                color = "#5f5"

                if reactant == False:
                    color = "yellow"

                if inputList[i-1][j-1] != "=>":
                    
                    canvas.create_rectangle(x0, y0, x1, y1, outline="#f11", fill=color, width=2)
                else:
                    reactant = False
                canvas.create_text(x1 - (width / 2), y1 - (height /2), font=('Helvetica','15','bold'),text=inputList[i - 1][j - 1])



        

        canvas.pack(fill=BOTH, expand=1)
# Determine the Maximum Column Number
# Input: Reaction_List
# Output: Max as Int
def getMaxColumn(reaction_list):
    max = 0
    for reaction in reaction_list:
        if len(reaction) > max:
            max = len(reaction)
    return max
    
# Main Method
def main():

    root = Tk()
    
    ex = Draw_Reaction()
    margin = 10
    height = 40
    width = 100
    reaction_list = Read_Compound_Reaction.get_reaction_list(Read_Compound_Reaction.readFile("Result2.txt"))

    inputList = Read_Compound_Reaction.get_reaction_data(reaction_list)
    inputList = Read_Compound_Reaction.get_compound_reaction(inputList)

    
    rows = len(inputList)
    column = getMaxColumn(inputList)
    windowHeight = (rows * margin + 2) + (height * rows + 2)
    windowWidth = (column * margin + 2) + (column * width + 2)
        
    height_width = "{}x{}+300+300".format(windowWidth, windowHeight)
    print(height_width)
    root.geometry(height_width)
    root.mainloop()


if __name__ == '__main__':
    main()

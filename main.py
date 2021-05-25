from tkinter import *
import numpy as np

matrixReact = []

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=",")
        print()

class chemReactNumber(Frame):
    numberArchiralSpecies = 0
    speciesReact = []
    achiralSpecies = []
    chemReact = []
    step = 0
    chemReactFrameIsFilled = False
    speciesFrameIsFilled = False
    reactionsFrameIsFilled = False
    noAchiralSpecies = 0
    noSpeciesStep2 = 0
    noSpeciesStep3 = 0
    noChemReacts = 0
    movesForward = False
    movesBackward = False

    def __init__(self, master=None):
        super().__init__(master)
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.rowconfigure(0, weight=10)
        master.rowconfigure(1, weight=1)
        self.master = master
        self.start()

    def start(self):
        self.startFrames()
        self.showStep(self.step)

    def startFrames(self):
        self.noChemReactFrame = Frame(root, bg="white")
        self.speciesFrame = Frame(root, bg="white")
        self.reactionsFrame = Frame(root, bg="white")
        self.achiralSpeciesFrame = Frame(root, bg="white")
        self.frameNav = Frame(root);

    def showStep(self, step):
        self.noChemReactFrame.grid_remove()
        self.speciesFrame.grid_remove()
        self.reactionsFrame.grid_remove()
        self.achiralSpeciesFrame.grid_remove()
        self.frameNav.grid_remove()

        if (step == 0):
            self.noChemReactFrame.grid(sticky="nsew", row=0, columnspan=2)
            if not self.chemReactFrameIsFilled:
                self.fillChemReactFrame(self.noChemReactFrame)
                self.chemReactFrameIsFilled = True

        elif (step == 1):
            self.speciesFrame.grid(sticky="nsew", row=0, columnspan=2)
            self.fillSpeciesFrame(self.speciesFrame)

        elif (step == 2):
            self.achiralSpeciesFrame.grid(sticky="nsew", row=0, columnspan=2)
            self.fillAchiralSpeciesFrame(self.achiralSpeciesFrame)

        elif (step == 3):
            self.reactionsFrame.grid(sticky="nsew", row=0, columnspan=2)
            self.fillChemReactionsFrame(self.reactionsFrame)
            self.reactionsFrameIsFilled = True

        else:
            self.makeChemEqMatrix()
            root.quit()

        self.fillFrameNav(self.frameNav)
        self.frameNav.grid(row=1)

    def fillFrameNav(self, frame):
        frame.grid()
        Button(root, text='Back', command=self.moveBackStep).grid(
            row=1, column=0, sticky='nesw', pady=10, padx=10)
        Button(root, text='Next', command=self.moveNextStep).grid(
            row=1, column=1, sticky='nesw', pady=10, padx=10)

    def moveNextStep(self):
        self.movesForward = True
        self.movesBackward = False
        self.step = self.step + 1
        self.showStep(self.step)

    def moveBackStep(self):
        self.movesForward = False
        self.movesBackward = True
        self.step = self.step - 1
        self.showStep(self.step)

    def fillChemReactFrame(self, frame):
        inputFrame = Frame(frame, bg="white")
        textField1 = Frame(inputFrame, bg="white")
        textField2 = Frame(inputFrame, bg="white")
        Label(textField1, text="Número de pareja enantioméricas:", bg="white").grid(sticky='nesw', row=0)
        self.numberSpecies = Entry(textField1, textvariable= StringVar(root, value='0'))
        self.numberSpecies.grid(sticky='nesw', row=1)
        Label(textField2, text="Número de especies aquirales:", bg="white").grid(sticky='nesw', row=2,column=0)
        self.numberArchiralSpecies = Entry(textField2, textvariable= StringVar(root, value='0'))
        self.numberArchiralSpecies.grid(row=4,column=0, sticky='nesw')
        frame.columnconfigure(0, weight=1)
        inputFrame.grid(pady=10)
        textField1.grid(pady=15, sticky='nesw')
        textField2.grid(pady=15, sticky='nesw')

    def fillAchiralSpeciesFrame(self, frame):
        if(int(self.numberArchiralSpecies.get())==0):
            if(self.movesForward):
                self.moveNextStep()
            if(self.movesBackward):
                self.moveBackStep()
        elif (self.noAchiralSpecies != int(self.numberArchiralSpecies.get())):
            self.noAchiralSpecies = int(self.numberArchiralSpecies.get())
            frame.grid()
            Label(frame, text="Nombre de especies aquirales:", bg="white").grid(row=0, pady=8)
            frameSpecies = Frame(frame, bg="white")
            rowSpecie = 1
            for noSpecie in range(self.noAchiralSpecies):
                if (noSpecie % 3 == 0):
                    rowSpecie = rowSpecie + 1
                    columnSpecies = 0
                Label(frameSpecies, text="Especie #%i:" % (noSpecie + 1), bg="white").grid(
                    row=rowSpecie, column=columnSpecies * 2)
                self.achiralSpecies.append(Entry(frameSpecies, width=10))
                self.achiralSpecies[noSpecie].grid(
                    row=rowSpecie, column=(columnSpecies * 2) + 1, padx=5, pady=5)
                columnSpecies = columnSpecies + 1
            frameSpecies.grid(sticky='nesw', pady=15, padx=15, row=1)
            frame.columnconfigure(0, weight=1)

    def fillSpeciesFrame(self, frame):
        if(int(self.numberSpecies.get())==0):
            if(self.movesForward):
                self.moveNextStep()
            if(self.movesBackward):
                self.moveBackStep()
        elif (self.noSpeciesStep2 != int(self.numberSpecies.get())):
            self.noSpeciesStep2 = int(self.numberSpecies.get())
            frame.grid()
            Label(frame, text="Nombre de especies enantioméricas:", bg="white").grid(row=0, pady=8)
            frameSpecies = Frame(frame, bg="white")
            rowSpecie = 1
            for noSpecie in range(self.noSpeciesStep2):
                if (noSpecie % 3 == 0):
                    rowSpecie = rowSpecie + 1
                    columnSpecies = 0
                Label(frameSpecies, text="Especie #%i:" % (noSpecie + 1), bg="white").grid(
                    row=rowSpecie, column=columnSpecies * 2)
                self.speciesReact.append(Entry(frameSpecies, width=10))
                self.speciesReact[noSpecie].grid(
                    row=rowSpecie, column=(columnSpecies * 2) + 1, padx=5, pady=5)
                columnSpecies = columnSpecies + 1
            frameSpecies.grid(sticky='nesw', pady=15, padx=15, row=1)
            frame.columnconfigure(0, weight=1)
            self.numberArchiralSpecies.grid(row=1)

    def fillReactionLabels(self,frame):
        column = 0
        columnReagent = 0
        columnProduct = 0

        for noSpecie in range(self.noSpeciesStep3):
            Label(
                frame,
                text="L%s" % self.speciesReact[noSpecie].get(),bg="white").grid(
                    row=0,
                    column=column)
            column=column+2

        for noSpecie in range(self.noSpeciesStep3):
            Label(
                frame,
                text="R%s" % self.speciesReact[noSpecie].get(),bg="white").grid(
                    row=0,
                    column=column)
            column=column+2

        for noSpecie in range(self.noAchiralSpecies):
            Label(
                frame,
                text=self.achiralSpecies[noSpecie].get(),bg="white").grid(
                    row=0,
                    column=column)
            column=column+2

        columnReagent=column
        column=column-1
        Label(frame, text="==>", bg="white").grid(row=0, column=column)
        column=column+1

        for noSpecie in range(self.noSpeciesStep3):
            Label(
                frame,
                text="L%s" % self.speciesReact[noSpecie].get(),bg="white").grid(
                    row=0,
                    column=column)
            column=column+2

        for noSpecie in range(self.noSpeciesStep3):
            Label(
                frame,
                text="R%s" % self.speciesReact[noSpecie].get(),bg="white").grid(
                    row=0,
                    column=column)
            column=column+2

        for noSpecie in range(self.noAchiralSpecies):
            Label(
                frame,
                text=self.achiralSpecies[noSpecie].get(),bg="white").grid(
                    row=0,
                    column=column)
            column = column+2

        columnProduct = column

        for col in range(1, columnReagent-1, 2):
            Label(frame,text="+",bg="white").grid(row=0,column=col)

        for col in range(columnReagent+1,columnProduct-1, 2):
            Label(frame,text="+",bg="white").grid(row=0,column=col)

    def fillChemReactionsFrame(self, frame):
        self.noSpeciesStep3 = int(self.numberSpecies.get())
        self.noAchiralSpecies = int(self.numberArchiralSpecies.get())
        Label(frame, text="Reacciones", bg="white").grid(pady=8, row=0)
        reactionsFrame = Frame(frame, bg="white")
        self.fillReactionLabels(reactionsFrame)
        AddBtn = Button(reactionsFrame, text="+", command=lambda: self.addReaction(reactionsFrame)).grid(row=100)
        reactionsFrame.grid(sticky='nesw', pady=15, padx=15, row=1)
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(0, weight=1)

    def addReaction(self,frame):
        self.chemReact.append([]);
        column=0
        for noSpecie in range((self.noSpeciesStep3*4)+(self.noAchiralSpecies*2)):
            self.chemReact[len(self.chemReact)-1].append(
                Entry(
                    frame,
                    width=5,
                    textvariable= StringVar(root, value='0')
                ))
            self.chemReact[len(self.chemReact)-1][noSpecie].grid(
                row=len(self.chemReact)+ 1,
                column=column,
                padx=5,
                pady=5)
            column = column+2

    def makeChemEqMatrix(self):
        matrixReact2=[]
        for i in range(len(self.chemReact)):
            matrixReact.append([])
            matrixReact2.append([])
            for j in range(len(self.chemReact[i])):
                matrixReact[i].append(self.chemReact[i][j].get())
                matrixReact2[i].append(0)
        p=len(matrixReact)

        for f in range(p):
            for k in range(self.noSpeciesStep2):
                n=matrixReact[f][k]
                m=matrixReact[f][k+self.noSpeciesStep2]
                matrixReact2[f][k+self.noSpeciesStep2]=n
                matrixReact2[f][k]=m

                n2 = matrixReact[f][k+self.noSpeciesStep2*2]
                m2 = matrixReact[f][k + (self.noSpeciesStep2*2)+self.noSpeciesStep2]
                matrixReact2[f][k + (self.noSpeciesStep2*2)+self.noSpeciesStep2] = n2
                matrixReact2[f][k+self.noSpeciesStep2*2] = m2
        matrixReact.extend(matrixReact2)

root = Tk()
root.minsize(600, 250)
root.title("ODE CHEM")
app = chemReactNumber(master=root)
app.mainloop()
root.destroy()
matrixReact = np.unique(matrixReact, axis=0)
matrixReact.tolist()

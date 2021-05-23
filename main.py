from tkinter import *

matrixReact = []


class chemReactNumber(Frame):
    numberChemReact = 0
    speciesReact = []
    chemReact = []
    step = 0
    chemReactFrameIsFilled = False
    speciesFrameIsFilled = False
    reactionsFrameIsFilled = False
    noSpeciesStep2 = 0
    noSpeciesStep3 = 0
    noChemReacts = 0

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
        self.frameNav = Frame(root);

    def showStep(self, step):
        self.noChemReactFrame.grid_remove()
        self.speciesFrame.grid_remove()
        self.reactionsFrame.grid_remove()
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
        self.step = self.step + 1
        self.showStep(self.step)

    def moveBackStep(self):
        self.step = self.step - 1
        self.showStep(self.step)

    def fillChemReactFrame(self, frame):
        inputFrame = Frame(frame, bg="white")
        textField1 = Frame(inputFrame, bg="white")
        textField2 = Frame(inputFrame, bg="white")
        Label(textField1, text="Número de pareja enantioméricas:", bg="white").grid(sticky='nesw', row=0)
        self.numberSpecies = Entry(textField1)
        self.numberSpecies.grid(sticky='nesw', row=1)
        Label(textField2, text="Number de reacciones:", bg="white").grid(row=2)
        self.numberChemReact = Entry(textField2)
        self.numberChemReact.grid(row=3, sticky='nesw')
        frame.columnconfigure(0, weight=1)
        inputFrame.grid(pady=10)
        textField1.grid(pady=15, sticky='nesw')
        textField2.grid(pady=15, sticky='nesw')

    def fillSpeciesFrame(self, frame):
        if (self.noSpeciesStep2 != int(self.numberSpecies.get())):
            self.noSpeciesStep2 = int(self.numberSpecies.get())
            frame.grid()
            Label(frame, text="Nombre de especies", bg="white").grid(row=0, pady=8)
            frameSpecies = Frame(frame, bg="white")
            rowSpecie = 1
            for noSpecie in range(self.noSpeciesStep2):
                if (noSpecie % 3 == 0):
                    rowSpecie = rowSpecie + 1
                    columnSpecies = 0
                Label(frameSpecies, text="Species #%i:" % (noSpecie + 1), bg="white").grid(
                    row=rowSpecie, column=columnSpecies * 2)
                self.speciesReact.append(Entry(frameSpecies, width=10))
                self.speciesReact[noSpecie].grid(
                    row=rowSpecie, column=(columnSpecies * 2) + 1, padx=5, pady=5)
                columnSpecies = columnSpecies + 1
            frameSpecies.grid(sticky='nesw', pady=15, padx=15, row=1)
            frame.columnconfigure(0, weight=1)
            self.numberChemReact.grid(row=1)

    def fillChemReactionsFrame(self, frame):
        if (self.noSpeciesStep3 != int(self.numberSpecies.get()) or
                self.noChemReacts != int(self.numberChemReact.get())):
            self.noSpeciesStep3 = int(self.numberSpecies.get())
            self.noChemReacts = int(self.numberChemReact.get())
            Label(frame, text="Reacciones", bg="white").grid(pady=8, row=0)
            reactionsFrame = Frame(frame, bg="white")

            for noSpecie in range(self.noSpeciesStep3):
                Label(reactionsFrame, text="L %s" % self.speciesReact[noSpecie].get(),bg="white").grid(
                    row=0, column=noSpecie)

            for noSpecie in range(self.noSpeciesStep3):
                Label(reactionsFrame, text="D %s" % self.speciesReact[noSpecie].get(),bg="white").grid(
                    row=0, column=(self.noSpeciesStep3 + noSpecie))

            Label(reactionsFrame, text="==>", bg="white").grid(row=0, column=(self.noSpeciesStep3 * 2))

            for noSpecie in range(self.noSpeciesStep3):
                Label(reactionsFrame, text="L %s" % self.speciesReact[noSpecie].get(), bg="white").grid(
                    row=0, column=(noSpecie + (self.noSpeciesStep3 * 2) + 1))

            for noSpecie in range(self.noSpeciesStep3):
                Label(reactionsFrame, text="D %s" % self.speciesReact[noSpecie].get(), bg="white").grid(
                    row=0, column=(noSpecie + self.noSpeciesStep3 + (self.noSpeciesStep3 * 2) + 1))

            for noChemReact in range(self.noChemReacts):
                self.chemReact.append([]);
                for noSpecie in range(self.noSpeciesStep3 * 2):
                    self.chemReact[noChemReact].append(Entry(reactionsFrame, width=5,textvariable= StringVar(root, value='0')))
                    self.chemReact[noChemReact][noSpecie].grid(
                        row=noChemReact + 1, column=noSpecie, padx=5, pady=5)

            for noChemReact in range(self.noChemReacts):
                for noSpecie in range(self.noSpeciesStep3 * 2):
                    self.chemReact[noChemReact].append(Entry(reactionsFrame, width=5,textvariable= StringVar(root, value='0')))
                    self.chemReact[noChemReact][noSpecie + (self.noSpeciesStep3 * 2)].grid(
                        row=(noChemReact) + 1, column=(noSpecie + (self.noSpeciesStep3 * 2)) + 1, padx=5, pady=5)

            reactionsFrame.grid(sticky='nesw', pady=15, padx=15, row=1)
            frame.rowconfigure(1, weight=1)
            frame.columnconfigure(0, weight=1)

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
        #print(matrixReact)


root = Tk()
root.minsize(600, 250)
root.title("ODE CHEM")
app = chemReactNumber(master=root)
app.mainloop()
root.destroy()
matrixReact
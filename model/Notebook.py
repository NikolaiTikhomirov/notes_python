from model.Note import Note

class Notebook:


    def __init__(self):
        """Конструктор"""
        self.notebook = []

    def addNoteToBook(self, note):
        self.notebook.append(note)
    
    def getNotesList(self):
        res = []
        for i in range(len(self.notebook)):
            res.append([Note.toString(self.notebook[i])])
        return res
    
    def getNotes(self):
        return self.notebook

    def toString(self):
        res = ""
        for i in range(len(self.notebook)):
            res += Note.toString(self.notebook[i]) + ";\n"
        return res
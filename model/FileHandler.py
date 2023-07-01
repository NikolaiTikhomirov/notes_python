import csv
from model.Note import Note
from model.Notebook import Notebook

class FileHandler:

    # def save(filePath, data):
    #     try:
    #         with open(filePath, 'w', newline='') as f:
    #             print(Notebook.getNotesList(data))
    #             writer = csv.writer(f)
    #             writer.writerows(Notebook.getNotesList(data))
    #     except:
    #         print("Сохранить не удалось")

    def save(filePath, notebook):
        try:
            with open(filePath, 'w', newline='') as f:
                fieldes = ['id', 'title', 'body', 'date']
                writer = csv.DictWriter(f, fieldnames=fieldes)
                writer.writeheader()
                id = ""
                title = ""
                body = ""
                date = ""
                notesList = Notebook.getNotes(notebook)
                for i in notesList:
                    id = i[0]
                    title = i[1]
                    body = i[2]
                    date = i[3]
                    writer.writerow({'id': id, 'title': title, 'body': body, 'date': date})
        except:
            print("Сохранить не удалось")
    

    def read(filePath):
        notebook = Notebook()
        notesList = Notebook.getNotes(notebook)
        try:
            with open(filePath, newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    # print(row)
                    Notebook.addNoteToBook(notebook, row)
                return notebook
        except:
            
            FileHandler.save(filePath, notebook)
            print("Создана новая записная книжка")
            return notebook

if __name__ == "__main__":
    pass
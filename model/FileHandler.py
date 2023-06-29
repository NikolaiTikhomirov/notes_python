import csv
from model.Note import Note
from model.Notebook import Notebook

class FileHandler:

    def save(filePath, data):
        try:
            with open(filePath, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        except:
            print("Сохранить не удалось")
    

    def read(filePath):
        notebook = Notebook()
        try:
            with open(filePath, newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    notebook.append(row)
                return notebook
        except:
            
            FileHandler.save(filePath, notebook)
            print("Создана новая записная книжка")
            return notebook

if __name__ == "__main__":
    pass
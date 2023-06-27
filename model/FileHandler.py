import csv
from model.Note import Note

class FileHandler:

    def save(filePath, data):
        try:
            with open('some.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        except:
            print("Сохранить не удалось")
    

    def read(filePath):
        try:
            with open(filePath, newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    print(row)
        except:
            note = Note()
            FileHandler.save(filePath, note)
            print("Создана новая записная книжка")
            return note

if __name__ == "__main__":
    pass
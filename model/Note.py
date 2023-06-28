

class Note:


    def __init__(self, id, title, body, date):
        """Конструктор"""
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    # def __init__(self):
    #     """Конструктор"""
    #     self.id = ""
    #     self.title = ""
    #     self.body = ""
    #     self.date = ""

    # Setters

    def settId(self, id):
        self.id = id
    
    def setTitle(self, title):
        self.title = title
    
    def setBody(self, body):
        self.body = body
    
    def setDate(self, date):
        self.date = date

    # Getters

    def getId(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
    def getBody(self):
        return self.body
    
    def getDate(self):
        return self.date

if __name__ == "__main__":
    pass
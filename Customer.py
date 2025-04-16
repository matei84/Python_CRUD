class Customer:

    def __init__(self, id="", name="", surname="", membership=0):
        self.name = name
        self.surname = surname
        self.membership = membership
        self.id = id


    def __str__(self):
        return f"Customer: id={self.id}, name={self.name}, surname={self.surname}, membership={self.membership}"  



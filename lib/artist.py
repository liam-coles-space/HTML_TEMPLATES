class Artist:
    # Attributes:
    #   id: int
    #   name: string
    #   genre: string
    def __init__(self,id, name, genre):
        self.id = id
        self.name = name
        self.genre = genre

    def __repr__(self):
        return f"Artist({self.id}, {self.name}, {self.genre})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def is_valid(self):
        if self.name == None or self.name == "":
            return False
        if self.genre == None or self.genre == "":
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.name == None or self.name == "":
            errors.append("Name cant be blank")
        if self.genre == None or self.genre == "":
            errors.append("Genre cant be blank")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
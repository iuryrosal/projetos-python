class DataDict:
    def __init__(self) -> None:
        self.database = {
            "0": "Iury",
            "1": "Davi",
            "2": "Vinicius"
          }
        
    def get_clients(self):
        return self.database
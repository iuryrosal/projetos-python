from data_dict import DataDict
from data_list import DataList

class AdapterListToDict(DataDict, DataList):
    def __init__(self) -> None:
        DataDict.__init__(self)
        DataList.__init__(self)
    
    def get_clients(self):
        database = {}
        id_ = 0
        for item in self.get_clients_list():
            database[f"{id_}"] = item
            id_ += 1
        return database
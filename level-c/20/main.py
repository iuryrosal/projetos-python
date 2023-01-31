from client_code import client_code
from data_dict import DataDict
from data_list import DataList
from adapter import AdapterListToDict

data = DataDict()
client_code(data)

data_list = DataList()
print(data_list.get_clients_list())

adapter = AdapterListToDict()
client_code(adapter)


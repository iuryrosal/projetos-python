class DatabaseClient:
  classmates = []
  connection = 0

  def __init__(self, port) -> None:
    self.set_connection(port)

  def set_connection(self, port):
    self.connection = port
  
  def get_connection(self):
    return self.connection
  
  def set_classmates(self, classmates):
    for classmate in classmates:
      self.classmates.append(classmate)

  def get_classmates(self):
    return self.classmates

if __name__ == "__main__":
  database_1 = DatabaseClient(1234)
  database_2 = DatabaseClient(4567)

  print(database_1.get_connection())

  print(database_2.get_connection())

  if database_1 == database_2:
    print("São iguais!")
  else:
    print("São distintas!")

  database_1.set_classmates(["Iury"])
  print(database_1.get_classmates())

  database_2.set_classmates(["Laura"])
  print(database_2.get_classmates())
  print(database_1.get_classmates())
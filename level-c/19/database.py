class DatabaseSingleton(type):
  _instances = {}

  def __call__(cls, *args, **kwds):
    if cls not in cls._instances:
      instance = super().__call__(*args, **kwds)
      cls._instances[cls] = instance
    return cls._instances[cls]


class DatabaseClient(metaclass=DatabaseSingleton):
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
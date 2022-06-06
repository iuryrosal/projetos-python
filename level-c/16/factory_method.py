from abc import ABC, abstractmethod

class Logistics:
  def createTransport(self):
    pass

  def planDelivery(self):
    transport = self.createTransport()

    result = f"Logistics: Transporte sendo preparado...\n{transport.deliver()}"

    return result

class RoadLogistics(Logistics):
  def __init__(self, name):
    self.name = name
  
  def createTransport(self):
    return Truck(self.name)

class SeaLogistics(Logistics):
  def __init__(self, name):
    self.name = name
  
  def createTransport(self):
    return Ship(self.name)

class Transport(ABC):
  @abstractmethod
  def deliver(self):
    pass

class Truck(Transport):
  def __init__(self, name):
    self.name = name
    self.category = "truck" 
  
  def deliver(self):
    result = (f"{self.category} preparado para entrega: {self.name}",
              "Transporte térreo....")
    return result

class Ship(Transport):
  def __init__(self, name):
    self.name = name
    self.category = "ship" 
  
  def deliver(self):
    result = (f"{self.category} preparado para entrega: {self.name}",
              "Transporte marítimo....")
    return result

def client_code(logistics: Logistics):
  print(f"App: Carregado com {logistics.__class__.__name__}.",
        f"{logistics.planDelivery()}")

if __name__ == "__main__":
  client_code(RoadLogistics("Caminhao1"))
  print("\n")
  client_code(SeaLogistics("Navio1"))
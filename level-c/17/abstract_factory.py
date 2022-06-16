from abc import ABC, abstractmethod

class AbstractApiFortal(ABC):
  def __init__(self, token):
    self.token = token 
  
  @abstractmethod
  def collect_data(self):
    pass

class ApiFortalTransport(AbstractApiFortal):
  def collect_data(self):
    return f"Dados Coletados ApiFortalTransport por meio do token: {self.token}"

class ApiFortalSecurity(AbstractApiFortal):
  def collect_data(self):
    return f"Dados Coletados ApiFortalSecurity por meio do token: {self.token}"

class AbstractApiCe(ABC):
  def __init__(self, token):
    self.token = token 
  
  @abstractmethod
  def collect_data(self):
    pass

  @abstractmethod
  def collect_data_by_city(self, city):
    pass

class ApiCeTransport(AbstractApiCe):
  def collect_data(self):
    return f"Dados Coletados ApiCeTransport por meio do token: {self.token}"
  
  def collect_data_by_city(self, city):
    return f"Dados Coletados da cidade {city} ApiCeTransport por meio do token: {self.token}"

class ApiCeSecurity(AbstractApiCe):
  def collect_data(self):
    return f"Dados Coletados ApiCeSecurity por meio do token: {self.token}"
  
  def collect_data_by_city(self, city):
    return f"Dados Coletados da cidade {city} ApiCeSecurity por meio do token: {self.token}"

class AbstractAPIFactory(ABC):
  def __init__(self, token_fortal, token_ce):
    self.token_fortal = token_fortal
    self.token_ce = token_ce
  
  @abstractmethod
  def create_api_fortal(self):
    pass

  @abstractmethod
  def create_api_ce(self):
    pass

class TransportDataFactory(AbstractAPIFactory):
  def create_api_fortal(self):
    return ApiFortalTransport(self.token_fortal)
  
  def create_api_ce(self):
    return ApiCeTransport(self.token_ce)

class SecurityDataFactory(AbstractAPIFactory):
  def create_api_fortal(self):
    return ApiFortalSecurity(self.token_fortal)
  
  def create_api_ce(self):
    return ApiCeSecurity(self.token_ce)

def client_code(factory: AbstractAPIFactory):
  product_fortal = factory.create_api_fortal()
  product_ce = factory.create_api_ce()

  print(product_fortal.collect_data())
  print(product_ce.collect_data_by_city("Iguatu"))

if __name__ == "__main__":
  token_ce = "ce12345"
  token_fortal = "fortal54321"

  print("Coletando dados de Transporte")
  client_code(TransportDataFactory(token_fortal, token_ce))
  
  print("Coletando dados de Segurança")
  client_code(SecurityDataFactory(token_fortal, token_ce))


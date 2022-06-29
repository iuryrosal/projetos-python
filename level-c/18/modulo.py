from abc import ABC, abstractmethod

class RequisicaoAPILinkedin:
  def __init__(self) -> None:
    self.req = {}

class RequisicaoAPIInstagram:
  def __init__(self) -> None:
    self.req = {}

class BuilderReq(ABC):
  @abstractmethod
  def reset():
    pass

  @abstractmethod
  def setQueryParams(filters):
    pass
  
  @abstractmethod
  def setDateRange(date_start, date_end):
    pass

  @abstractmethod
  def setPermission(permission):
    pass

  @abstractmethod
  def setEndpoint():
    pass

  @abstractmethod
  def getRequest():
    pass

class BuilderReqLinkedin(BuilderReq):
  def __init__(self) -> None:
    self.reqAPI = self.reset()
  
  def reset(self):
    return RequisicaoAPILinkedin()
  
  def setQueryParams(self, filters):
    query_params = ""
    for filter_, value in filters.items():
      query_params += f"&{filter_}={value}"
    self.reqAPI.req["QueryParams"] = query_params
  
  def setDateRange(self, date_start, date_end):
    self.reqAPI.req["DateRange"] = f"DateStart={date_start}&DateEnd={date_end}"
  
  def setPermission(self, permission):
    self.reqAPI.req["Permission"] = f"/{permission}/"
  
  def setEndpoint(self):
    link = "https://www.linkedin.com/company/86297503/api"
    self.reqAPI.req["endpoint"] = link + self.reqAPI.req["Permission"] + self.reqAPI.req["DateRange"] + self.reqAPI.req["QueryParams"]

  def getRequest(self):
    return self.reqAPI.req

class BuilderReqInstagram(BuilderReq):
  def __init__(self) -> None:
    self.reqAPI = self.reset()
  
  def reset(self):
    return RequisicaoAPIInstagram()
  
  def setQueryParams(self, filters):
    query_params = ""
    for filter_, value in filters.items():
      query_params += f"&{filter_}={value}"
    self.reqAPI.req["QueryParams"] = query_params
  
  def setDateRange(self, date_start, date_end):
    self.reqAPI.req["DateRange"] = f"Date_In={date_start}&Date_End={date_end}"
  
  def setPermission(self, permission):
    self.reqAPI.req["Permission"] = f"/{permission}/"
  
  def setEndpoint(self):
    link = "https://www.instagram.com/account/86297503/api/"
    self.reqAPI.req["endpoint"] = link + self.reqAPI.req["Permission"] + self.reqAPI.req["DateRange"] + self.reqAPI.req["QueryParams"]

  def getRequest(self):
    return self.reqAPI.req

class Director:
  def __init__(self, request) -> None:
    self.request_user = request
  
  def ConstructReqLinkedin(self, builder):
    builder.reset()
    builder.setQueryParams(self.request_user["filter"])
    builder.setDateRange(self.request_user["data_inicio"], self.request_user["data_fim"])
    builder.setPermission(self.request_user["permissao"])
    builder.setEndpoint()
  
  def ConstructReqInstagram(self, builder):
    builder.reset()
    builder.setQueryParams(self.request_user["filter"])
    builder.setDateRange(self.request_user["data_inicio"], self.request_user["data_fim"])
    builder.setPermission(self.request_user["permissao"])
    builder.setEndpoint()


if __name__ == "__main__":
  input_user = {
    "name": "Iury Rosal",
    "origem": "Linkedin",
    "permissao": "FOLLOWERS",
    "data_inicio": "2021-12-31",
    "data_fim": "2021-01-01",
    "filter": {
      "Title_Contain": "Dados",
      "Quant_Exp": ">3"
    }
  }

  director = Director(input_user)

  if input_user["origem"] == "Linkedin":
    builder = BuilderReqLinkedin()
    director.ConstructReqLinkedin(builder)
    request = builder.getRequest()
  elif input_user["origem"] == "Instagram":
    builder = BuilderReqInstagram()
    director.ConstructReqInstagram(builder)
    request = builder.getRequest()
  else:
    print("Origem desconhecida!")
  print(request)